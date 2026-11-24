# API-First Video Dashboard

This is a small video dashboard. A Flask API stores video details in MongoDB and a React app shows them as a list on a dashboard.

## What it does

- `GET /video/dashboard` returns active videos (up to 2 right now)
- `POST /video/create` adds a video (title, description, YouTube id, thumbnail)
- `GET /video/<id>/stream` returns a playback token and a video file URL
- `POST /auth/signup`, `POST /auth/login` and `GET /auth/me` using JWT tokens
- `GET /api/healthz` for a simple health check
- Flask serves the thumbnail images from `backend/static`
- The React app calls the API and shows the videos

## Tech used

Python, Flask, Flask-JWT-Extended, PyMongo, MongoDB, React (Create React App)

## How to run

You need MongoDB running. The backend reads these environment variables (see `backend/.env.example`):

- `MONGO_URI`
- `SECRET_KEY`
- `JWT_SECRET_KEY`
- `PORT` (optional, default 5000)

The app does not load a `.env` file by itself, so set them in your shell first, for example:

```bash
cd backend
export MONGO_URI=mongodb://localhost:27017
export SECRET_KEY=some-local-value
export JWT_SECRET_KEY=another-local-value
pip install -r requirements.txt
python app.py
```

The API runs on http://127.0.0.1:5000.

```bash
cd frontend
npm install
npm start
```

The app runs on http://localhost:3000. Note that `frontend/src/api/api.js` points `BASE_URL` at my deployed backend, so change it to `http://127.0.0.1:5000` to use your local API.

## What I would improve

- No tests for the backend yet
- `POST /video/create` saves a YouTube id, but the dashboard and stream routes still build URLs from a local `video_filename`, so these two parts do not match yet
- The API base URL in the frontend should come from an environment variable
