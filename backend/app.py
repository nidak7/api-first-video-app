from flask import Flask
from config import Config
from extensions import init_db
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__, static_folder="static", static_url_path="/static")
    app.config.from_object(Config)

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
    port = int(os.environ.get("PORT", 5000))  # use Render's PORT, fallback 5000
    app.run(host="0.0.0.0", port=port, debug=True)