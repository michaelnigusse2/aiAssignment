
from PyQt6.QtWidgets import QGraphicsLineItem, QGraphicsSimpleTextItem
from PyQt6.QtGui import QPen, QBrush, QColor
from PyQt6.QtCore import Qt


class EdgeItem(QGraphicsLineItem):
    def __init__(self, node_a, node_b, x1, y1, x2, y2, cost, parent=None):
        super().__init__(x1, y1, x2, y2, parent)
        self.node_a = node_a
        self.node_b = node_b
        self.cost = cost
        pen = QPen(QColor("#4e4e4e"))
        pen.setWidth(2)
        self.setPen(pen)
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2
        self.cost_text = QGraphicsSimpleTextItem(str(int(cost)))
        self.cost_text.setBrush(QBrush(QColor("#1565c0")))
        self.cost_text.setPos(mid_x - 8, mid_y - 12)

    def highlight(self):
        p = QPen(QColor("#ff9800"))
        p.setWidth(4)
        self.setPen(p)

    def unhighlight(self):
        p = QPen(QColor("#4e4e4e"))
        p.setWidth(2)
        self.setPen(p)
