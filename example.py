import sys

try:
    from PyQt6.QtGui import QIcon
    from PyQt6.QtWidgets import QApplication
except ModuleNotFoundError:
    from PySide6.QtGui import QIcon
    from PySide6.QtWidgets import QApplication

from custom_window import CustomWindow


class ExampleWindow(CustomWindow):
    def __init__(self):
        super().__init__(use_mica='if available', theme='auto', color="F2F2F299")
        self.resize(640, 480)
        self.setWindowTitle("Very example")
        self.setWindowIcon(QIcon("example_icon.png"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example_win = ExampleWindow()
    example_win.show()
    sys.exit(app.exec())
