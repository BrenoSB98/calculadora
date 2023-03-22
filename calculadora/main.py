# type: ignore
import sys

from constraints import WINDOW_ICON_PATH
from display import Display
from info import Info
from main_winfow import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from style import setupTheme

if __name__ == '__main__':
    # Create Application
    app = QApplication(sys.argv)

    window = MainWindow()

    # Define Icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    setupTheme()
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('854 + 566 = 1420')
    window.addToVLayout(info)

    # Display
    display = Display()
    window.addToVLayout(display)

    # Run All
    window.adjustFixedSize()
    window.show()
    app.exec()
