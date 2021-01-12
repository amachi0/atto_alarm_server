import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging
from firebase_admin.exceptions import FirebaseError
from firebase_admin.messaging import Message, Notification
from src.util import error as app_error
from src.util.response_code import ResponseCode

def initialize_firebase():
    try:
        cred = credentials.Certificate("firebase-adminsdk.json")
        firebase_admin.initialize_app(cred)
    except Exception:
        raise app_error.CannotInitializeApp("Cannot initialize fcm.", ResponseCode.UNAUTHORIZED)

def send_message_to_topic(topic: str, title: str, body: str) -> str:
    message = Message(
        notification=Notification(
            title=title,
            body=body
        ),
        topic=topic
    )

    try:
        return messaging.send(message)
    except ValueError:
        raise app_error.CannotSendMessage(
            "Message arguments are invalid.",
            ResponseCode.INTERNAL_SERVER_ERROR)
    except FirebaseError:
        raise app_error.CannotSendMessage(
            "error occurs while sending the message to the FCM service.",
            ResponseCode.INTERNAL_SERVER_ERROR)
