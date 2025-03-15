# Base da imagem
FROM python:3.10

# Definir qual será o diretório de trabalho de APP -> Container
WORKDIR /app 

# Copiar o arquivo de config dependências
COPY requirements.txt requirements.txt

COPY iss_tracker.py app.py

# Instalando as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Execução de entrada do container/app
CMD [ "python", "app.py" ]