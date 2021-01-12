import requests
from bs4 import BeautifulSoup
from src.common.scrape_util import get_text_from_class, get_rate, get_date
from src.util import error as app_error
from src.util.response_code import ResponseCode

def scrape_from_atcoder():
    try:
        r = requests.get('https://atcoder.jp?lang=ja')
    except requests.exceptions.RequestException:
        raise app_error.CannotRequestAtcoder("Cannot request atcoder.", ResponseCode.NOT_FOUND)

    if not r.ok:
        raise app_error.CannotRequestAtcoder("Response is invalid.", ResponseCode.NOT_FOUND)

    soup = BeautifulSoup(r.content, "html.parser")
    list_contest = soup.find(
        'ul', {'class': 'm-list_contest'})

    contests = []
    for li in list_contest.find_all('li'):
        name = get_text_from_class(li, "m-list_contest_ttl")
        status = get_text_from_class(li, "status")
        time = get_date(get_text_from_class(li, "time"))
        target_rate = get_rate(get_text_from_class(li, "rated"))
        contest = {
            "name": name,
            "status": status,
            "time": time,
            "target_rate": target_rate
        }
        contests.append(contest)

    return contests
