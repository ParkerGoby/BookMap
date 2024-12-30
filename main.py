import sys
from PyQt6.QtWidgets import QApplication, QWidget

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Basic Window")
        self.setGeometry(100, 100, 400, 300)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())