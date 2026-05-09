from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy() 

class Notification(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100))
    message=db.Column(db.String(300))
    type=db.Column(db.String(50))
    is_read=db.Column(db.Boolean,default=False)
    created_at=db.Column(db.DateTime,default=datetime.utcnow)       