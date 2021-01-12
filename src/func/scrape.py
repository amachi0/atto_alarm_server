from src.logic.scrape_from_atcoder import scrape_from_atcoder
from src.util import error as app_error
from src.util.response import success, failure
from src.util.response_code import ResponseCode


def scrape_atcoder(event, context):
    try:
        contests = {
            "response": scrape_from_atcoder()
        }
        return success(contests, ResponseCode.OK)

    except app_error.AppException as e:
        return failure(e)
