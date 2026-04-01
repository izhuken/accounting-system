from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QLabel, QProgressBar, QVBoxLayout, QWidget

from core.config.app import Config
from shared.colors import Colors

# from shared.lib import Toaster


class InitPage(QWidget):
    navigate = Signal(str)

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(10)

        title = QLabel("Проводим настройку приложения...")
        title.setStyleSheet(
            """
            QLabel {
                font-size: 16px;
                font-weight: 400;
                color: %s;
            } 
        """
            % Colors.TEXT_DARK.value
        )
        layout.addWidget(title)

        progress_bar = QProgressBar()
        progress_bar.setRange(0, 0)
        progress_bar.setFixedSize(400, 10)
        progress_bar.setStyleSheet(
            """
        QProgressBar {
            border: 1px solid %s;
            border-radius: 5px;
        }
                                   
        QProgressBar::chunk {
            background-color: %s;
            width: 10px;
            margin: 0px;
        }
        """
            % (Colors.GRAY_DISABLED.value, Colors.BLUE_DARK.value)
        )

        layout.addWidget(progress_bar, alignment=Qt.AlignCenter)
        self.setLayout(layout)

        self.init_db()

    def init_db(self) -> None:
        print(
            Config.db_url,
            Config.db_path,
        )
