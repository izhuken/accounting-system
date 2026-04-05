from typing import Any

from PySide6.QtCore import QObject, Signal


class IThreadCommand(QObject):
    finished = Signal()

    def execute(self, payload: Any, *args, **kwargs) -> None:
        raise NotImplementedError
