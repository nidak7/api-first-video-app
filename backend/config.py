import os

class Config:
    # set these in your environment (see .env.example), the defaults are only for local testing
    SECRET_KEY = os.getenv("SECRET_KEY", "change-me-in-env")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "change-me-in-env")
