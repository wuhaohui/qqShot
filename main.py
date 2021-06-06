import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from screenshot import ScreenShot


if __name__ == "__main__":
    # QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    qtApp = QApplication(sys.argv)
    window = ScreenShot()
    window.show()
    qtApp.exec()

