# Gunakan image Python resmi
FROM python:3.11-slim

# Set direktori kerja di dalam container
WORKDIR /app

# Install dependency sistem
RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    libssl-dev \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Pastikan pip sudah terinstal dan diperbarui ke versi terbaru
RUN python -m ensurepip && \
    pip install --upgrade pip==25.1.1

# Salin file requirements.txt dan install dependency Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --retries 10 --timeout 30 --default-timeout=60

# Salin semua file source code
COPY . .

# Expose port aplikasi FastAPI (gunakan 5001 seperti yang kamu minta)
EXPOSE 5001

# Jalankan server menggunakan Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5001"]
