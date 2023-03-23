from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Basic Layout
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        # Window Title
        self.setWindowTitle('Calculator')

    # Function to adjust fixed size
    def adjustFixedSize(self):
        # Last Command
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    # Function to add widget to Layout
    def addWidgetsToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)
