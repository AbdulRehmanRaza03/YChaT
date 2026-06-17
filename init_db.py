"""Run once to create all tables: python init_db.py"""
import os
from app import create_app
from app.models import db

app = create_app(os.environ.get("FLASK_ENV", "development"))

with app.app_context():
    db.create_all()
    print("✅ All tables created successfully.")
    print("Tables:", list(db.engine.table_names()))
