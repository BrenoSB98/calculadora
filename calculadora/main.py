# type: ignore
import sys

from constraints import WINDOW_ICON_PATH
from display import Display
from main_winfow import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

if __name__ == '__main__':
    # Create Application
    app = QApplication(sys.argv)
    window = MainWindow()

    # Define Icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Display
    display = Display()
    window.addToVLayout(display)

    # Run All
    window.adjustFixedSize()
    window.show()
    app.exec()
