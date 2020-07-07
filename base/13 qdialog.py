from PyQt5 import QtCore, QtGui, QtWidgets

class DrawWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(DrawWidget, self).__init__(*args, **kwargs)
        self.setFixedSize(640, 480)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setBrush(QtGui.QBrush(QtCore.Qt.darkMagenta))
        painter.setPen(QtCore.Qt.NoPen)
        path = QtGui.QPainterPath()
        path.addText(QtCore.QPoint(10, 100), QtGui.QFont("Times", 40, QtGui.QFont.Bold), "Stack Overflow and Qt")
        painter.drawPath(path)

class Dialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        scroll_area = QtWidgets.QScrollArea(widgetResizable=True)
        draw_widget = DrawWidget()
        scroll_area.setWidget(draw_widget)
        lay = QtWidgets.QVBoxLayout(self)
        lay.addWidget(scroll_area)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Dialog()
    w.resize(320, 240)
    w.show()
    sys.exit(app.exec_())