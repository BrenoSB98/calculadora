from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Basic Layout
        self.cw = QWidget()
        self.view_layout = QVBoxLayout()
        self.cw.setLayout(self.view_layout)
        self.setCentralWidget(self.cw)

        # Window Title
        self.setWindowTitle('Calculator')

    # Function to adjust fixed size
    def adjustFixedSize(self):
        # Last Command
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    # Function to add widget to Layout
    def addWidgetToVLayout(self, widget: QWidget):
        self.view_layout.addWidget(widget)
        self.adjustFixedSize()
