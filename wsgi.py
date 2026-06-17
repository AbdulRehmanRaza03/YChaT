import os
from app import create_app, socketio
from flask_dance.contrib.google import make_google_blueprint

app = create_app(os.environ.get("FLASK_ENV", "production"))

google_bp = make_google_blueprint(
    client_id=app.config.get("GOOGLE_CLIENT_ID"),
    client_secret=app.config.get("GOOGLE_CLIENT_SECRET"),
    scope=[
        "openid",
        "https://www.googleapis.com/auth/userinfo.email",
        "https://www.googleapis.com/auth/userinfo.profile",
    ],
    redirect_url="/auth/google/callback",
)
app.register_blueprint(google_bp, url_prefix="/auth")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    socketio.run(app, host="0.0.0.0", port=port)
