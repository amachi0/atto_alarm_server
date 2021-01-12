import os
from datetime import timezone, timedelta

class Const:
    JST = timezone(timedelta(hours=9), "JST")
    SECONDS_OF_ONE_HOUR = 3600

    MORNING_TOPIC = os.environ['MORNING_TOPIC']
    ONE_HOUR_AGO_TOPIC = os.environ['ONE_HOUR_AGO_TOPIC']

    WEB_HOOK_URL = os.environ['SLACK_WEB_HOOK_URL']
