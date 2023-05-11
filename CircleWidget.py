from PySide2 import QtWidgets, QtGui
from PySide2.QtGui import QPainter, QPen, Qt, QBrush


class CircleWidget(QtWidgets.QFrame):

    def __init__(self, color):
        super(CircleWidget, self).__init__()
        self.color = color

    def paintEvent(self, arg__1: QtGui.QPaintEvent) -> None:
        super().paintEvent(arg__1)
        painter = QPainter(self)
        painter.setBrush(QBrush(self.color, Qt.SolidPattern))
        painter.drawEllipse(5, 5, 90, 90)
