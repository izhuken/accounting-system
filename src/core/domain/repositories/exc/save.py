class SaveException(Exception):
    def __init__(self, message: str = "Ошибка сохранения данных") -> None:
        self.message = message
        super().__init__(self.message)
