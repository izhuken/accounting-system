class AuthenticationException(Exception):
    def __init__(self, message: str = "Ошибка авторизации! Неверный пароль!") -> None:
        self.message = message
        super().__init__(self.message)
