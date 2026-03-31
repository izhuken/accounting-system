from PySide6.QtCore import QEasingCurve, QPropertyAnimation, Qt, QTimer
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget


class Toaster(QWidget):
    def __init__(self, message, duration=3000, parent=None):
        super().__init__(parent)
        self.setWindowFlags(
            Qt.ToolTip | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_ShowWithoutActivating)

        self.label = QLabel(message)
        self.label.setStyleSheet("""
            background-color: rgba(50, 50, 50, 220);
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 12pt;
        """)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        self.adjustSize()

        QTimer.singleShot(duration, self.hide_toast)

        self.opacity_anim = QPropertyAnimation(self, b"windowOpacity")
        self.opacity_anim.setDuration(300)
        self.opacity_anim.setStartValue(0)
        self.opacity_anim.setEndValue(1)
        self.opacity_anim.setEasingCurve(QEasingCurve.InOutQuad)
        self.opacity_anim.start()

    def show_toast(self, x=None, y=None):
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        if x is None:
            x = screen_geometry.width() - self.width() - 20
        if y is None:
            y = screen_geometry.height() - self.height() - 20
        self.move(x, y)
        self.show()

    def hide_toast(self):
        self.opacity_anim = QPropertyAnimation(self, b"windowOpacity")
        self.opacity_anim.setDuration(300)
        self.opacity_anim.setStartValue(1)
        self.opacity_anim.setEndValue(0)
        self.opacity_anim.setEasingCurve(QEasingCurve.InOutQuad)
        self.opacity_anim.finished.connect(self.close)
        self.opacity_anim.start()
