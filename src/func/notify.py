from src.model.notify_status import NotifyState
from src.util.response_code import ResponseCode
from src.logic.scrape_from_atcoder import scrape_from_atcoder
from src.logic.notify import get_notify_status, notify_to_fcm
from src.util import error as app_error
from src.util.response import success, failure

def notify_one_hour(event, context):
    try:
        contests = scrape_from_atcoder()
        notify_status = get_notify_status(contests, False)

        if notify_status == NotifyState.NOTHING:
            return success({'response': 'recent contest is nothing'}, ResponseCode.NO_CONTENT)
        else:
            message_id = notify_to_fcm(notify_status)
            return success(
                {'response': f"sent a message to FCM. message_id: {message_id}"},
                ResponseCode.OK)
    except app_error.AppException as e:
        return failure(e)

def notify_morning(event, context):
    try:
        contests = scrape_from_atcoder()
        notify_status = get_notify_status(contests, True)

        if notify_status == NotifyState.NOTHING:
            return success({'response': 1}, ResponseCode.NO_CONTENT)
        else:
            message_id = notify_to_fcm(notify_status)
            return success(
                {'response': f"sent a message to FCM. message_id: {message_id}"},
                ResponseCode.OK)
    except app_error.AppException as e:
        return failure(e)
