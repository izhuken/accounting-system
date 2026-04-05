from PySide6.QtCore import Slot

from core.service.app import InitDBService

from .ithreadcommand import IThreadCommand


class InitThreadCommand(IThreadCommand):
    @Slot()
    def execute(self):
        init_service = InitDBService()
        init_service.init_db()
        self.finished.emit()
