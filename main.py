import os
import sys

from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtGui import QGuiApplication


def main():
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('main.qml')
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
