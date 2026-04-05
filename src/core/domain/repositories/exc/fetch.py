class FetchException(Exception):
    def __init__(self, message: str = "Ошибка загрузки данных") -> None:
        self.message = message
        super().__init__(self.message)
