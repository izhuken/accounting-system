class InitialException(Exception):
    def __init__(self, message: str = "Ошибка инициализации приложения!") -> None:
        self.message = message
        super().__init__(self.message)
