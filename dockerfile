# Usamos a imagem oficial do Python como a imagem base
FROM python:3

# Configurar variáveis de ambiente para evitar problemas de codificação
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Instala as dependências do projeto (o arquivo requirements.txt precisa estar na mesma pasta que o Dockerfile)
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código do projeto para o diretório de trabalho no container
COPY . /app/
