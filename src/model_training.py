import os
import sys
import pandas as pd
# import joblib
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import (
    accuracy_score, precision_score,
    recall_score, f1_score
)
import lightgbm as lgb
from src.logger import get_logger
from src.custom_exception import CustomException
from config.paths_config import *
from config.model_params import *
from utils.common_functions import read_yaml, load_data
from scipy.stats import randint
import mlflow
import mlflow.sklearn

logger = get_logger(__name__)


config_file_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml')

try:
    config_data = read_yaml(config_file_path)
except Exception as e:
    logger.error(f"ERROR: Failed to load config.yaml for experiment naming: {e}")
    sys.exit(1) # Termina o script se não conseguir carregar a configuração

bucket_file_name = config_data['data_ingestion']['bucket_file_name']
experiment_name = f"ML_Experiment_{bucket_file_name.replace('.csv', '')}"



mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment(experiment_name)



class ModelTraining:
    def __init__(self, train_path, test_path, model_output_path):
        self.train_path = train_path
        self.test_path = test_path
        self.model_output_path = model_output_path

        self.params_dist = LIGHTGBM_PARAMS
        self.random_search_params = RANDOMSEARCH_PARAMS


    def load_and_split_data(self):
        try:
            logger.info(f"Loading data from {self.train_path}")
            train_df = load_data(self.train_path)

            logger.info(f"Loading data from {self.test_path}")
            test_df = load_data(self.test_path)

            X_train = train_df.drop(columns=['booking_status'])
            y_train = train_df['booking_status']

            X_test = test_df.drop(columns=['booking_status'])
            y_test = test_df['booking_status']

            logger.info("Data splitted successfully for Model Training")

            return X_train, y_train, X_test, y_test
        
        except Exception as e:
            logger.error(f"Error while loading data {e}")
            raise CustomException(f"Failed to load data{e}", sys)
        

    def train_lgbm(self, X_train, y_train):
        try:
            logger.info("Initializing our model")

            lgbm_model = lgb.LGBMClassifier(
                random_state=self.random_search_params["random_state"]
            )

            logger.info("Starting our hyperparams tuning")

            random_search = RandomizedSearchCV(
                estimator= lgbm_model,
                param_distributions= self.params_dist,
                n_iter= self.random_search_params["n_iter"],
                cv= self.random_search_params["cv"],
                n_jobs= self.random_search_params["n_jobs"],
                verbose= self.random_search_params["verbose"],
                random_state= self.random_search_params["random_state"],
                scoring= self.random_search_params['scoring']
            )

            random_search.fit(X_train, y_train)

            logger.info("Hyperparams tuning completed")

            best_params = random_search.best_params_
            best_model = random_search.best_estimator_

            logger.info(f"Best parameters are: {best_params}")

            return best_model, best_params
        
        except Exception as e:
            logger.error(f"Error while training model {e}")
            raise CustomException(f"Failed to train model {e}", sys)

    def evaluate_model(self, model, X_test, y_test):
        try:
            logger.info("Evaluating our model")

            y_pred = model.predict(X_test)

            accuracy = accuracy_score(y_test, y_pred)
            precision = precision_score(y_test, y_pred)
            recall = recall_score(y_test, y_pred)
            f1 = f1_score(y_test, y_pred)

            logger.info(f"Accuracy: {accuracy}")
            logger.info(f"Precision: {precision}")
            logger.info(f"Recall: {recall}")
            logger.info(f"f1: {f1}")

            return {
                "accuracy": accuracy,
                "precision": precision,
                "recall": recall,
                "f1": f1
            }
        
        except Exception as e:
            logger.error(f"Error while evaluating model {e}")
            raise CustomException(f"Failed to evaluate model {e}", sys)
        

    # def save_model(self, model):
    #     try:
    #         logger.info("trying to save model")

    #         os.makedirs(os.path.dirname(self.model_output_path), exist_ok=True)

    #         logger.info("saving the model")
    #         joblib.dump(model, self.model_output_path)

    #         logger.info(f"Model saved to {self.model_output_path}")
        
    #     except Exception as e:
    #         logger.error(f"Error while saving model {e}")
    #         raise CustomException(f"Failed to save model {e}", sys)
        

    def run(self):
        try:
            with mlflow.start_run(run_name="LightGBM_RandomSearch_v1"):
                logger.info("Starting our Model Training Pipeline")
                logger.info("Starting our MLFLOW EXPERIMENTATION")

                mlflow.set_tag("developer", "Zeygler")
                mlflow.set_tag("model_type", "LightGBM")
                mlflow.set_tag("dataset_version", "v1.0_processed")

                logger.info("Logging the training and testing dataset to MLFLOW")
                mlflow.log_artifact(self.train_path, artifact_path='datasets')
                mlflow.log_artifact(self.test_path, artifact_path='datasets')


                X_train, y_train, X_test, y_test = self.load_and_split_data()
                best_model, best_params = self.train_lgbm(X_train, y_train)
                metrics = self.evaluate_model(best_model, X_test, y_test)
                # self.save_model(best_model)

                input_example = X_train.head(1)

                logger.info("Logging the model into MLFLOW")
                mlflow.sklearn.log_model(
                    best_model, name="model",registered_model_name="HotelReservationModel",
                    input_example=input_example
                )


                mlflow.log_params(best_params)
                mlflow.log_metrics(metrics)

                logger.info("Model Training sucesfully completed")

        except Exception as e:
            logger.error(f"Error in model training pipeline {e}")
            raise CustomException(f"Failed during model training pipeline {e}", sys)
        

if __name__ == '__main__':
    trainer = ModelTraining(
        PROCESSED_TRAIN_DATA_PATH, PROCESSED_TEST_DATA_PATH, MODEL_OUTPUT_PATH
    )
    trainer.run()