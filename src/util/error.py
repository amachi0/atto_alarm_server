class AppException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code

    def __str__(self):
        return repr(self.message)

class FCMException(AppException):
    pass

class CannotInitializeApp(FCMException):
    pass

class CannotSendMessage(FCMException):
    pass


class ScrapingException(AppException):
    pass

class CannotRequestAtcoder(ScrapingException):
    pass
