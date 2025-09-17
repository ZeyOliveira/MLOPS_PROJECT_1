# Use uma imagem base Python leve
FROM python:slim

# Define variáveis de ambiente para Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Instala dependências do sistema operacional (libgomp1 para scikit-learn/xgboost)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copia o arquivo de requisitos e instala as dependências Python
# É uma boa prática copiar apenas o requirements.txt primeiro para aproveitar o cache do Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código da sua aplicação para o contêiner
# Isso inclui pipeline/, src/, application.py, etc.
COPY . .

# Define uma variável de ambiente para o MLflow Tracking URI
# Isso é um valor padrão. Ele será sobrescrito na execução do contêiner.
ENV MLFLOW_TRACKING_URI=http://localhost:5000

# Expõe a porta 5000, provavelmente para o seu aplicativo Flask (application.py)
EXPOSE 5000

# Comando padrão para executar quando o contêiner for iniciado
# Este é o seu aplicativo Flask, que servirá as previsões.
CMD ["python", "application.py"]