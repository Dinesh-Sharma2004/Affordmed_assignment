from flask import Flask 
from config import Config
app=Flask(__name__)
app.config.from_object(Config)
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logging_middleware.logging_config import setup_logging
setup_logging(app)
from app.middleware.error_handler import register_error_handlers
register_error_handlers(app)

from app.models.notification_model import db

db.init_app(app)
with app.app_context():
    db.create_all()

from app.routes.notification_routes import notification_bp
app.register_blueprint(notification_bp)

@app.route('/')
def home():
    
    return {"message":"Backend Running"}

if __name__=="__main__":
    app.run(debug=True)
