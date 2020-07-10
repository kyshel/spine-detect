from PyQt5 import QtGui, QtCore
from PyQt5 import QtWidgets, uic

from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
                             QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
                             QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
                             QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
                             QVBoxLayout, QWidget,QScrollArea, QMainWindow)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button = QPushButton()
        self.button.clicked.connect(self.handleButton)
        self.button.setIcon(QtGui.QIcon('../png/t/study0/image1.dcm.png'))
        self.button.setIconSize(QtCore.QSize(24,24))
        layout = QVBoxLayout()
        layout.addWidget(self.button)

    def handleButton(self):
        pass


if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())