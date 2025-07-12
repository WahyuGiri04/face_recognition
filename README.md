
# 🧠 Face Verification API with FastAPI + DeepFace (ArcFace)

API sederhana untuk membandingkan dua wajah dan memverifikasi apakah mereka adalah orang yang sama. Menggunakan `DeepFace` dengan model `ArcFace` dan framework `FastAPI`.

---

## 🚀 Fitur

- 🔍 Verifikasi wajah berbasis AI
- ⚡ FastAPI (cepat dan ringan)
- 🎯 Menggunakan model `ArcFace` (akurat dan efisien)
- 🖼️ Input berupa gambar **Base64**
- 🧪 Swagger UI otomatis untuk uji coba

---

## 🧰 Dependencies

Pastikan Python 3.8+ sudah terpasang, lalu install dependensi:

```bash
pip install fastapi uvicorn deepface opencv-python-headless numpy tf-keras
```

---

## 🏁 Menjalankan Server

```bash
uvicorn app.main:app --host 0.0.0.0 --port 5001 --reload
```

---

## 🔬 Endpoint

### `POST /verify`

Verifikasi dua gambar wajah.

**Request Body (JSON):**
```json
{
  "img1": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD...",
  "img2": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD..."
}
```

> Catatan: Jika gambar memiliki prefix `data:image/jpeg;base64,`, tetap boleh dikirim — API akan membersihkannya otomatis.

**Response (JSON):**
```json
{
  "verified": true,
  "distance": 0.456,
  "threshold": 0.68,
  "model": "ArcFace",
  "detector_backend": "opencv"
}
```

---

## 🧪 Swagger UI

Akses dokumentasi interaktif di:
```
http://localhost:5001/docs
```

---

## ⚙️ Konfigurasi Model & Deteksi

- **Model:** `ArcFace`
- **Detector:** `opencv` (cepat dan ringan)
- **Detection:** `enforce_detection=False`

---

## 📦 Struktur Project

```
face-verification-api/
├── main.py
└── README.md
```

---

## 🧠 Credit

- [DeepFace](https://github.com/serengil/deepface)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)

---

## 📌 Lisensi

MIT License © 2025


---

## 📄 Membuat & Menggunakan `requirements.txt`

### 🎯 1. Generate `requirements.txt`
Jika virtual environment sudah berisi semua library, jalankan:

```bash
pip freeze > requirements.txt
```

Ini akan membuat file `requirements.txt` berisi semua dependensi yang dibutuhkan.

### 📥 2. Install dari `requirements.txt`

Untuk menginstal semua library dari file tersebut:

```bash
pip install -r requirements.txt
```

> Pastikan kamu menjalankannya di dalam virtual environment (`venv`) agar tidak mengganggu sistem Python utama.



---

## 🧪 Virtual Environment (venv)

### 🔧 1. Membuat Virtual Environment

Jalankan perintah berikut (gantilah `venv` dengan nama folder jika mau):

```bash
python3 -m venv venv
```

### 🚀 2. Aktivasi Virtual Environment

- **Linux / macOS:**
  ```bash
  source venv/bin/activate
  ```

- **Windows:**
  ```bash
  .\venv\Scripts\activate
  ```

Setelah aktivasi, terminal akan menampilkan prefix `(venv)`.

### 🛑 3. Menonaktifkan (Deactivate)

Untuk keluar dari virtual environment:

```bash
deactivate
```

## 🛠️ Build & Run with Docker

### 🔧 1. Build the Docker image
 ```bash
  docker build -t face-recognition:1.0.0 .
  ```

### 🚀 2. Run the container
```bash
  docker run -d -p 5001:5001 --name face-recognition face-recognition:1.0.0
  ```
