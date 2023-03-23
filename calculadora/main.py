import sys

from buttons import ButtonsGrid
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
    setupTheme()
    window = MainWindow()

    # Define Icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('')
    window.addWidgetsToVLayout(info)

    # Display
    display = Display()
    window.addWidgetsToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # Run All
    window.adjustFixedSize()
    window.show()
    app.exec()
