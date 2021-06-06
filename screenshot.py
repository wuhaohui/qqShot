from PyQt5.QtCore import QRect, QPoint, QRectF, QSize, QLineF, QPointF, QEventLoop
from PyQt5.QtGui import QColor, QPainterPath, QKeySequence, QGuiApplication, QPixmap, QPen, QBrush, QImage, QPainter, \
    QPolygonF, QClipboard, QCursor, QMouseEvent
from PyQt5.QtWidgets import QGraphicsView, QApplication, QGraphicsScene, QShortcut, QFileDialog, QDialog


class ScreenShot(QGraphicsView):
    def __init__(self):
        super(ScreenShot, self).__init__()

        self.screenPixel = None
        self.graphics_scene = None

        self.setShortcut()  # 设置快捷键
        self.fullScreenShot()

    def setShortcut(self):
        QShortcut(QKeySequence('esc'), self).activated.connect(self.close)

    def close(self):
        super().close()

    def fullScreenShot(self):
        screen = QGuiApplication.screenAt(QCursor.pos())
        self.screenPixel = screen.grabWindow(0)
        # self.screenPixel.

        self.graphics_scene = QGraphicsScene(0, 0, self.screenPixel.width(), self.screenPixel.height())

        # self.show()
        self.setScene(self.graphics_scene)
        print(QCursor.pos())
        self.windowHandle().setScreen(QGuiApplication.screenAt(QCursor.pos()))
        self.show()

        # print(self.screenPixel)
        self.setGeometry(QGuiApplication.screenAt(QCursor.pos()).geometry())
        self.showFullScreen()
