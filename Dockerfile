# Vulnerable Dockerfile - For Educational Purposes
# Contains intentional security misconfigurations

FROM python:3.9

# Container runs as root because no USER instruction is defined

RUN apt-get update && apt-get install -y \
    curl \
    wget \
    vim \
    net-tools \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

EXPOSE 5000

CMD python src/vulnerable_app.py
