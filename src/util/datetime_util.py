from datetime import datetime, timedelta
from src.util.const import Const

def is_morning(datetimeNow: datetime) -> bool:
    return True if datetimeNow.hour == 9 else False


def delta_time_to_contest(datetimeStr: str, datetimeNow: datetime) -> timedelta:
    datetimeContest = datetime.strptime(datetimeStr, '%Y-%m-%d %H:%M:%S').astimezone(Const.JST)
    return datetimeContest - datetimeNow
