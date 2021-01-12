from datetime import datetime
from src.util.const import Const
from src.util.datetime_util import delta_time_to_contest
from src.model.notify_status import NotifyState
from src.common.fcm import initialize_firebase, send_message_to_topic

def get_notify_status(contests, isMorning) -> NotifyState:
    datetimeNow = datetime.now(Const.JST)

    for contest in contests:
        if contest['status'] != '予定':
            continue

        deltaToContest = delta_time_to_contest(contest['time'], datetimeNow)
        if deltaToContest.days != 0 or deltaToContest.seconds < 0:
            continue
        if isMorning:
            return NotifyState.TODAY
        if deltaToContest.seconds <= Const.SECONDS_OF_ONE_HOUR:
            return NotifyState.ONE_HOUR_AGO

    return NotifyState.NOTHING

def notify_to_fcm(notifyState: NotifyState) -> str:
    initialize_firebase()
    message_id = 'empty'

    if notifyState == NotifyState.TODAage_to_toY:
        message_id = send_message_to_topic(Const.MORNING_TOPIC, '', '本日開催のコンテストがあります！')

    elif notifyState == NotifyState.ONE_HOUR_AGO:
        message_id = send_message_to_topic(Const.ONE_HOUR_AGO_TOPIC, '', 'もうすぐコンテストが開始されます！')

    return message_id

