class RemoveException(Exception):
    def __init__(
        self,
        message: str = "Ошибка. Перед удалением записи убедитесь, что она не используется в других объектах.",
    ) -> None:
        self.message = message
        super().__init__(self.message)
