# type: ignore
import sys

from main_winfow import MainWindow
from PySide6.QtWidgets import QApplication, QLabel

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    label1 = QLabel('O tectonic')
    window.addWidgetToVLayout(label1)

    window.show()
    app.exec()
