from flask import Flask
from config import Config
from extensions import init_db
from flask_jwt_extended import JWTManager
from flask_cors import CORS

def create_app():
    app = Flask(__name__, static_folder="static", static_url_path="/static")
    app.config.from_object(Config)
    CORS(app)

    db = init_db()

    jwt = JWTManager(app)

    from routes.auth_routes import auth_bp
    from routes.video_routes import video_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(video_bp)

    @app.route("/api/healthz")
    def health():
        return {"ok": True}
    
    return app

if __name__ == "__main__":
    app = create_app()
