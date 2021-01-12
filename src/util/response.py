import json
import requests
import traceback
from src.util.error import AppException
from src.util.const import Const

def success(body: dict, code: int) -> dict:
    return {
        'statusCode': code,
        'body': json.dumps(body)
    }


def failure(exception: AppException) -> dict:
    requests.post(
        Const.WEB_HOOK_URL,
        data=json.dumps({
            "text": f"response code: {exception.code}\n"
                    f"message: {exception.message}\n"
                    f"stack_trace: {traceback.format_exc()}"})
    )
    return {
        'statusCode': exception.code,
        'body': json.dumps({"result": exception.message})
    }
