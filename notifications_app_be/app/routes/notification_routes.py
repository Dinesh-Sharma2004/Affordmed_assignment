from flask import Blueprint
from flask import request

from app.services.notification_service import NotificationService

notification_bp = Blueprint('notification_bp', __name__)

@notification_bp.route('/notifications', methods=['GET'])
def get_notifications():
    notifications = NotificationService.get_all_notifications()
    data=[]
    for n in notifications:
        data.append({"id":n.id,"title":n.title,"message":n.message,"type":n.type,"is_read":n.is_read,"created_at":n.created_at})
        return {"notifications":data}
    

@notification_bp.route('/notifications/send', methods=['POST'])
def send_notification():
    body=request.json
    notification=NotificationService.create_notification(body)
    return {"notification":{"id":notification.id,"title":notification.title,"message":notification.message,"type":notification.type,"is_read":notification.is_read,"created_at":notification.created_at}}

@notification_bp.route('/notifications/<int:notification_id>/read', methods=['PATCH'])
def mark_read(notification_id):
    notification=NotificationService.mark_as_read(notification_id)
    if not notification:
        return {"error":"Notification not found"},404
    return {"message":"Notification marked as read"},200

@notification_bp.route('/notifications/<int:notification_id>', methods=['DELETE'])
def delete_notification(notification_id):
    notification=NotificationService.delete_notification(notification_id)
    if not notification:
        return {"error":"Notification not found"},404
    return {"message":"Notification deleted"},200
