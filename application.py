import numpy as np
from flask import Flask, render_template, request
import joblib
from config.paths_config import MODEL_OUTPUT_PATH

app = Flask(__name__)


try:
    loaded_model = joblib.load(MODEL_OUTPUT_PATH)
    print(f"Modelo carregado com sucesso de: {MODEL_OUTPUT_PATH}")
except FileNotFoundError:
    print(f"ERRO: Modelo não encontrado em {MODEL_OUTPUT_PATH}. Verifique o caminho.")
    loaded_model = None

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction_result = None

    if request.method == 'POST':
        if loaded_model is None:
            
            return render_template('index.html', prediction=None, error_message="Erro: Modelo de ML não carregado. Verifique o log do servidor.")

        try:
            
            lead_time = int(request.form['lead_time'])
            
            no_of_special_requests = int(request.form['no_of_special_requests'])
            avg_price_per_room = float(request.form['avg_price_per_room']) # Preço pode ser float
            arrival_month = int(request.form['arrival_month'])
            arrival_date = int(request.form['arrival_date'])
            market_segment_type = int(request.form['market_segment_type'])
            no_of_week_nights = int(request.form['no_of_week_nights'])
            no_of_weekend_nights = int(request.form['no_of_weekend_nights'])
            type_of_meal_plan = int(request.form['type_of_meal_plan'])
            room_type_reserved = int(request.form['room_type_reserved'])

            
            features = np.array([[
                lead_time,
                no_of_special_requests,
                avg_price_per_room,
                arrival_month,
                arrival_date,
                market_segment_type,
                no_of_week_nights,
                no_of_weekend_nights,
                type_of_meal_plan,
                room_type_reserved,
            ]])

            prediction = loaded_model.predict(features)
            prediction_result = prediction[0] 

        except KeyError as e:
            
            print(f"KeyError: field '{e}' not found in request POST.")
            return render_template('index.html', prediction=None, error_message=f"Error: incomplete form data, check the fields: {e}")
        except ValueError as e:
            
            print(f"ValueError: error converting data type: {e}")
            return render_template('index.html', prediction=None, error_message=f"Error: Invalid data format. Please enter valid numbers. Details: {e}")
        except Exception as e:
            
            print(f"unexpected error during prediction: {e}")
            return render_template('index.html', prediction=None, error_message=f"an unexpected error occurred: {e}")

    
    return render_template('index.html', prediction=prediction_result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)