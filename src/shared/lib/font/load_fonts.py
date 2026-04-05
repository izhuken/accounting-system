from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtWidgets import QApplication


def load_fonts(app: QApplication):
    fonts = [
        ":/fonts/Inter_18pt-Black.ttf",
        ":/fonts/Inter_18pt-BlackItalic.ttf",
        ":/fonts/Inter_18pt-Bold.ttf",
        ":/fonts/Inter_18pt-BoldItalic.ttf",
        ":/fonts/Inter_18pt-ExtraBold.ttf",
        ":/fonts/Inter_18pt-ExtraBoldItalic.ttf",
        ":/fonts/Inter_18pt-ExtraLight.ttf",
        ":/fonts/Inter_18pt-ExtraLightItalic.ttf",
        ":/fonts/Inter_18pt-Italic.ttf",
        ":/fonts/Inter_18pt-Light.ttf",
        ":/fonts/Inter_18pt-LightItalic.ttf",
        ":/fonts/Inter_18pt-Medium.ttf",
        ":/fonts/Inter_18pt-MediumItalic.ttf",
        ":/fonts/Inter_18pt-Regular.ttf",
        ":/fonts/Inter_18pt-SemiBold.ttf",
        ":/fonts/Inter_18pt-SemiBoldItalic.ttf",
        ":/fonts/Inter_18pt-Thin.ttf",
        ":/fonts/Inter_18pt-ThinItalic.ttf",
    ]

    for font in fonts:
        QFontDatabase.addApplicationFont(font)

    app.setFont(QFont("Inter", 12))
