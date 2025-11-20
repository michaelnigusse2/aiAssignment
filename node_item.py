# node_item.py
from PyQt6.QtWidgets import (
    QGraphicsEllipseItem,
    QGraphicsTextItem,
    QGraphicsItem
)
from PyQt6.QtGui import QBrush, QColor, QPen
from PyQt6.QtCore import Qt, QVariantAnimation

R = 18

class NodeItem(QGraphicsEllipseItem):
    def __init__(self, name, x, y, radius=R, parent=None):
        super().__init__(-radius, -radius, 2 * radius, 2 * radius, parent)

        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, False)

        self.name = name
        self.setPos(x, y)

        self.default_brush = QBrush(QColor("white"))
        self.setBrush(self.default_brush)
        self.setPen(QPen(QColor("black")))

        self.text = QGraphicsTextItem(name, self)
        self.text.setDefaultTextColor(QColor("black"))
        self.text.setPos(-radius, -radius - 20)

        self.anim = QVariantAnimation()
        self.anim.valueChanged.connect(self._apply_scale)

    def _apply_scale(self, v):
        self.setScale(v)

    def animate_hover(self):
        self.anim.stop()
        self.anim.setStartValue(self.scale())
        self.anim.setEndValue(1.15)
        self.anim.setDuration(200)
        self.anim.start()

    def animate_unhover(self):
        self.anim.stop()
        self.anim.setStartValue(self.scale())
        self.anim.setEndValue(1.0)
        self.anim.setDuration(200)
        self.anim.start()

    def set_default(self):
        self.setBrush(self.default_brush)

    def set_closed(self):
        self.setBrush(QBrush(QColor("#d3d3d3")))

    def set_frontier(self):
        self.setBrush(QBrush(QColor("#fff176")))  

    def set_path(self):
        self.setBrush(QBrush(QColor("#66bb6a")))  

    def set_current(self):
        self.setBrush(QBrush(QColor("#ef5350")))  
