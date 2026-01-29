# API-First Video Dashboard

A simple **API-first video dashboard** built with **Flask + MongoDB** (backend) and **React** (frontend). The backend exposes clean APIs to fetch video metadata and serves static assets (videos/thumbnails). The frontend consumes these APIs to display a dashboard and play videos.

---

## 🔧 Tech Stack

**Backend**

* Python 3.11
* Flask
* PyMongo
* MongoDB

**Frontend**

* React (CRA)
* Fetch API

---

## 📁 Project Structure

```
backend/
 ├── app.py
 ├── routes/
 ├── models/
 ├── static/
 │   ├── thumbnails/
 │   └── videos/
 └── venv/

frontend/
 ├── src/
 │   ├── App.js
 │   └── components/
 └── package.json
```

---

## 🗄️ Database Schema (MongoDB)

**Collection:** `videos`

Example document:

```json
{
  "title": "SQL for Beginners",
  "description": "Start learning SQL",
  "thumbnail_url": "sql.png",
  "video_url": "sql_intro.mp4",
  "is_active": true,
  "created_at": "2026-01-29T08:34:52Z"
}
```

> Note: `thumbnail_url` and `video_url` store **file names only**. The backend constructs full URLs.

---

## 🚀 Backend Setup

### 1️⃣ Create virtual environment

```bash
cd backend
python -m venv venv
venv\Scripts\activate
```

### 2️⃣ Install dependencies

```bash
pip install flask pymongo flask-cors
```

### 3️⃣ Start MongoDB

Ensure MongoDB is running locally on default port (`27017`).

### 4️⃣ Run backend server

```bash
python app.py
```

Backend runs at:

```
http://127.0.0.1:5000
```

---

## 📡 API Endpoints

### 🔹 GET /video/dashboard

Returns all active videos for dashboard.

**Response:**

```json
[
  {
    "id": "697b1bacde0cf0f1fc8029bb",
    "title": "Python for Beginners",
    "description": "Start coding in Python",
    "thumbnail_url": "http://127.0.0.1:5000/static/thumbnails/python.png",
    "video_url": "http://127.0.0.1:5000/static/videos/python_intro.mp4"
  }
]
```

---

## 🖥️ Frontend Setup

### 1️⃣ Install dependencies

```bash
cd frontend
npm install
```

### 2️⃣ Start frontend

```bash
npm start
```

Frontend runs at:

```
http://localhost:3000
```

---

## 🎥 Video Playback

* Videos are stored locally in `backend/static/videos/`
* Thumbnails are stored in `backend/static/thumbnails/`
* Flask serves static files
* React `<video>` tag streams videos via backend URL

---

## ✅ Features Implemented

* API-first architecture
* MongoDB-based video storage
* Dashboard API
* Video playback
* Static file serving
* Clean separation of frontend & backend

---

## 🎯 Assignment Status

✔ Backend APIs implemented
✔ Database connected
✔ Videos playable
✔ Frontend dashboard functional
✔ Meets assignment requirements

---

## 📌 Notes

* Thumbnail display issues do **not** affect core requirements
* Focus is on API design and video playback

---

# Note for evaluators
The `backend/static/videos/` folder is empty due to GitHub file size limits.
To test video playback:

1. Download small sample videos (e.g., Python intro, SQL intro) 
   and place them inside `backend/static/videos/`.
2. Update MongoDB documents if needed to match the file names.


## 👩‍💻 Author

**Nida Khan**

---

