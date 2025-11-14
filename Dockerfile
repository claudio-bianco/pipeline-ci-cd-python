FROM python:3.12-slim

# Evita buffering e problemas de encoding
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Instala dependências do sistema (opcional, mas útil para builds)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copia requirements e instala deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY app ./app

EXPOSE 8000

# Comando para subir a API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

