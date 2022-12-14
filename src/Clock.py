from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from datetime import datetime
import math

class Clock(QWidget):
    def __init__(self, parent_container):
        super().__init__()
        
        self.container = parent_container
        
        self.hour = datetime.now().hour
        self.minute = datetime.now().second

        self.set_clock_radius(400, 400)

    def set_clock_radius(self, new_x_radius=200, new_y_radius=200):
        self.clock_x_radius = new_x_radius
        self.clock_y_radius = new_y_radius

    def update_time(self):
        self.hour = datetime.now().hour
        self.minute = datetime.now().minute
        self.update()

    def draw_clock(self, painter):
        self.canvas_horizontal_mid = int(self.container.size().width() / 2)
        self.canvas_vertical_mid = int(self.container.size().height() / 2)

        painter.drawEllipse(int(self.canvas_horizontal_mid - self.clock_x_radius - 10), int(self.canvas_vertical_mid - self.clock_y_radius), int(self.clock_x_radius * 2), int(self.clock_y_radius * 2))

        self.font = QtGui.QFont()
        self.font.setPointSize(15)
        painter.setFont(self.font)
        for i in range(12):
            self.hour_angle = ((-2*math.pi*i) + (6 * math.pi)) / 12

            self.start_x = self.canvas_horizontal_mid
            self.start_y = self.canvas_vertical_mid
            
            self.hour_stop_x = self.start_x + int((0.85 * self.clock_x_radius) * math.cos(self.hour_angle))
            self.hour_stop_y = self.start_y - int((0.85 * self.clock_y_radius) * math.sin(self.hour_angle))
            
            # painter.drawText(self.hour_stop_x - 7, self.hour_stop_y + 7, str(i))
            painter.drawText(self.hour_stop_x - 22, self.hour_stop_y - 12, 25, 18, Qt.AlignCenter, str(i))
    
    def update_hourhand(self, painter, start_x, start_y):
        self.hour_angle = ((-2*math.pi*self.hour) + (6 * math.pi)) / 12
        self.hour_stop_x = start_x + int((0.6 * self.clock_x_radius) * math.cos(self.hour_angle))
        self.hour_stop_y = start_y - int((0.6 * self.clock_y_radius) * math.sin(self.hour_angle))
        painter.drawLine(start_x, start_y, self.hour_stop_x, self.hour_stop_y)

    def update_minutehand(self, painter, start_x, start_y):
        self.minute_angle = ((-2*math.pi*self.minute) + (30 * math.pi)) / 60
        self.minute_stop_x = start_x + int((0.7 * self.clock_x_radius) * math.cos(self.minute_angle))
        self.minute_stop_y = start_y - int((0.7 * self.clock_y_radius) * math.sin(self.minute_angle))
        painter.drawLine(start_x, start_y, self.minute_stop_x, self.minute_stop_y)

    def paintEvent(self, event):
        # print("In paint event")
        self.pen = QtGui.QPen()
        self.pen.setColor(QtGui.QColor("white"))
        self.pen.setWidth(2)
        painter = QPainter(self)
        painter.setPen(self.pen)


        canvas_horizontal_mid = int(self.container.size().width() / 2)
        canvas_vertical_mid = int(self.container.size().height() / 2)

        print(f"Current x radius: {self.clock_x_radius}")
        print(f"Current y radius: {self.clock_y_radius}")
        print(f"Current container width: {self.container.size().width()}")
        print(f"Current container height: {self.container.size().height()}")
        print(f"Setting clock radius to {self.container.size().width()}")
        self.set_clock_radius(int(self.container.size().width() * 0.4), self.container.size().height() * 0.4)

        self.draw_clock(painter)

        # painter.drawEllipse(int(canvas_horizontal_mid - self.clock_x_radius - 5), int(canvas_vertical_mid - self.clock_y_radius), int(self.clock_x_radius * 2), int(self.clock_y_radius * 2))

        start_x = self.canvas_horizontal_mid - 10
        start_y = self.canvas_vertical_mid

        # painter.drawPoint(canvas_horizontal_mid, canvas_vertical_mid)
        self.update_hourhand(painter, start_x, start_y)
        self.update_minutehand(painter, start_x, start_y)
