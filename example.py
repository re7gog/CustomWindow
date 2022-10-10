import sys

try:
    from PySide6.QtGui import QIcon
    from PySide6.QtWidgets import QApplication
except ModuleNotFoundError:
    from PyQt6.QtGui import QIcon
    from PyQt6.QtWidgets import QApplication

from custom_window import CustomWindow


class ExampleWindow(CustomWindow):
    def __init__(self):
        super().__init__()
        self.resize(640, 480)
        self.setWindowTitle("Very example")
        self.setWindowIcon(QIcon("example_icon.png"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example_win = ExampleWindow()
    example_win.show()
    sys.exit(app.exec())
