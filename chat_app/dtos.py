from chat_app.models import User


class RegistrationRequest:
    def __init__(self):
        self.__user: User = None
        self.__otp: str = ""

    def setUser(self, user: User) -> None:
        self.__user = user

    def getUser(self) -> User:
        return self.__user

    def setOtp(self, otp: str) -> None:
        self.__otp = otp

    def getOtp(self) -> str:
        return self.__otp
