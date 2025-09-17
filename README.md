[![author](https://img.shields.io/badge/Zeygler&nbsp;Oliveira-red.svg)](https://www.linkedin.com/in/zeygler-oliveira-a021a92a4/)
[![](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)

# Previsão de Cancelamento de Reservas Hoteleiras: Um Projeto MLOps End-to-End

Este repositório é o resultado de uma jornada completa, desde a coleta de dados até a implantação de um modelo em produção, tudo orquestrado com as melhores práticas de Machine Learning Operations (MLOps).

Meu objetivo aqui é mostrar como transformei um problema de negócio real em uma solução robusta e escalável, utilizando um pipeline de ML completo.

## O Problema e a Solução

Imagine um hotel que não consegue prever quais reservas serão canceladas. Isso gera quartos vazios inesperados, perda de receita e dificuldade no planejamento. Meu projeto visa resolver exatamente isso:

**O Desafio:** Prever se um cliente irá honrar sua reserva ou cancelar.

**A Solução:** Um modelo de Machine Learning preditivo, integrado em um pipeline MLOps, que permite ao hotel tomar decisões proativas, otimizar a ocupação e maximizar a receita.

## A Jornada do Projeto: Workflow MLOps

Este projeto foi construído seguindo um workflow MLOps detalhado, garantindo que cada etapa do ciclo de vida do modelo fosse gerenciada de forma eficiente e automatizada. Aqui está um resumo dessa jornada, passo a passo:

### 1. **Database Setup (Configuração do Banco de Dados)**
*   **O que foi feito:** Preparamos o ambiente para armazenar nossos dados de reserva.
*   **Por que é importante:** Um banco de dados bem estruturado é a base para qualquer projeto de dados, garantindo que as informações estejam organizadas e acessíveis.
*   **Ferramenta:** **Google Cloud**, mais especificamente o uso de Buckets.

### 2. 🚀 **Project Setup (Configuração do Projeto)**
*   **O que foi feito:** Estruturamos o ambiente de desenvolvimento, definindo dependências e a organização do código.
*   **Por que é importante:** Garante que o projeto seja replicável, fácil de manter e que todos os colaboradores possam rodar sem problemas.
*   **Ferramentas/Conceitos:** Python, `venv` (ambiente virtual), `requirements.txt` (gerenciamento de dependências), `setup.py` (empacotamento do projeto).

### 3. 📥 **Data Ingestion (Ingestão de Dados)**
*   **O que foi feito:** Desenvolvemos scripts para coletar e carregar os dados brutos das reservas.
*   **Por que é importante:** É o primeiro contato com os dados! Garantir que a ingestão seja limpa e eficiente é crucial para a qualidade de todo o pipeline.
*   **Habilidades:** Scripting em Python, manipulação de dados.

### **Data Processing (Processamento de Dados)**
*   **O que foi feito:** Limpamos, transformamos e preparamos os dados brutos para o treinamento do modelo. Isso inclui tratamento de valores ausentes, engenharia de features e codificação de variáveis.
*   **Por que é importante:** Dados de qualidade são importantes para o modelo.
*   **Habilidades:** Python (Pandas, NumPy), pré-processamento de dados, engenharia de features.

### **Model Training (Treinamento do Modelo)**
*   **O que foi feito:** Selecionamos e treinamos o modelo de Machine Learning para prever o status da reserva.
*   **Por que é importante:** Aqui é onde a mágica acontece! O modelo aprende padrões nos dados para fazer previsões precisas.
*   **Habilidades:** Machine Learning (Scikit-learn, etc.), avaliação de modelos, otimização de hiperparâmetros.

### **Jupyter Notebook Testing (Testes em Jupyter Notebook)**
*   **O que foi feito:** Utilizamos Jupyter Notebooks para explorar os dados (EDA), prototipar modelos e testar ideias rapidamente.
*   **Por que é importante:** Permite experimentação ágil e documentação interativa do processo de desenvolvimento.
*   **Ferramentas/Conceitos:** Jupyter Notebook (`notebook` folder), **Análise Exploratória de Dados (EDA)**.

### **Experiment Tracking (Rastreamento de Experimentos)**
*   **O que foi feito:** Registramos experimentos de treinamento de modelos, incluindo métricas, parâmetros e artefatos.
*   **Por que é importante:** Essencial para a reprodutibilidade e para saber qual modelo performou melhor e por quê.
*   **Ferramentas/Conceitos:** **MLflow** (`mlruns`, `mlartifacts` folders) – uma ferramenta fantástica para gerenciar o ciclo de vida do ML.

  ![Mlflow](https://github.com/ZeyOliveira/MLOPS_PROJECT_1/blob/main/docs/screenshots/mlflow_params_metrics.png)
  ![Mlflow](https://github.com/ZeyOliveira/MLOPS_PROJECT_1/blob/main/docs/screenshots/mlflow_experiments_page.png)
  


### **Training Pipeline (Pipeline de Treinamento)**
*   **O que foi feito:** Automatizamos todo o processo de treinamento do modelo, desde a ingestão até o registro do modelo.
*   **Por que é importante:** Garante que o modelo possa ser retreinado de forma consistente e automática com novos dados, mantendo sua relevância ao longo do tempo.
*   **Habilidades:** Orquestração de pipelines, scripting Python (`pipeline` folder).

### **Data Versioning (Versionamento de Dados)**
*   **O que foi feito:** Implementamos um sistema para versionar os datasets utilizados no treinamento.
*   **Por que é importante:** Tão importante quanto versionar o código! Garante que possamos reproduzir resultados e entender como as mudanças nos dados afetam o modelo.
*   **Ferramentas/Conceitos:** Git e Github(para metadados), Google Cloud Storage.

### **CI-CD Deployment (Implantação Contínua e Entrega Contínua)**
*   **O que foi feito:** Criamos um pipeline de CI/CD para automatizar a construção, teste e implantação do modelo e da aplicação.
*   **Por que é importante:** Leva o modelo do laboratório para o mundo real! Garante que novas versões do modelo ou da aplicação sejam entregues de forma rápida e segura.
*   **Ferramentas/Conceitos:** **Jenkins** (`Jenkinsfile`, `custom_jenkins` folder), **Docker** (`Dockerfile`), **Google Cloud** (para implantação e gerenciamento de recursos).

  ![Jenkins](https://github.com/ZeyOliveira/MLOPS_PROJECT_1/blob/main/docs/screenshots/jenkins_pipeline_stage_view.png)
  

### **User App Building (Construção da Aplicação do Usuário)**
*   **O que foi feito:** Desenvolvemos uma interface simples para que os usuários possam interagir com o modelo e obter previsões.
*   **Por que é importante:** O modelo só tem valor se puder ser usado! Uma aplicação amigável torna a inteligência artificial acessível.
*   **Ferramentas/Conceitos:** Python (Flask/HTML/CSS), desenvolvimento web (`application.py`, `static`, `templates` folders).

### **Code Versioning (Versionamento de Código)**
*   **O que foi feito:** Gerenciamos todas as alterações de código usando Git.
*   **Por que é importante:** Colaboração, rastreabilidade e a capacidade de reverter para versões anteriores são fundamentais em qualquer projeto de software.
*   **Ferramentas/Conceitos:** **Git** (`.gitignore`), GitHub.

## 🚀 Como Ver o Projeto em Ação


*   **Registro de Monitoramento:** [Logs](https://github.com/ZeyOliveira/MLOPS_PROJECT_1/blob/main/logs/log_2025-09-16.log)
*   **Screenshots:** Mostrando as partes importantes de interfaces UI locais: [Screenshots](https://github.com/ZeyOliveira/MLOPS_PROJECT_1/tree/main/docs/screenshots)
*   **Instruções de Execução:** Detalhes sobre como configurar o ambiente e rodar o projeto localmente (ou acessar a versão deployada, se aplicável).


