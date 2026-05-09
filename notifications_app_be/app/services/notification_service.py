from app.models.notification_model import Notification
from app.models.notification_model import db

class NotificationService:
    @staticmethod
    def get_all_notifications():
        return Notification.query.all()

    @staticmethod
    def create_notification(data):
        notification=Notification(title=data["title"],message=data["message"],type=data["type"])
        db.session.add(notification)
        db.session.commit()
        return notification
    
    @staticmethod
    def mark_as_read(notification_id):
        notification=Notification.query.get(notification_id)
        notification.is_read=True
        db.session.commit()
        return notification
    
    @staticmethod
    def delete_notification(notification_id):
        notification=Notification.query.get(notification_id)
        if not notification:
            return None
        db.session.delete(notification)
        db.session.commit()
        return notification
