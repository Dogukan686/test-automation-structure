
FROM python:3.10-slim

# Gerekli paketleri yükle
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# Allure için gerekli bağımlılık
RUN apt-get update && apt-get install -y openjdk-11-jre-headless && rm -rf /var/lib/apt/lists/*

# Kodu kopyala
COPY . /app
WORKDIR /app

# Varsayılan komut: behave çalıştır
CMD ["behave", "-f", "pretty"]
