#!/usr/bin/env python
# encoding: utf-8
'''
 @author: Hengheng Zhang
 @contact: hengheng.zhang@Kit.edu
 @file: WeatherSensor.py
 @time: 7/16/2021 12:51 PM
 @Function: WeatherSensor
'''
from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg
import sys
from random import randint
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pyqtgraph.Qt import QtGui, QtCore
from PyQt5.QtCore import Qt

class WeatherSensor(QWidget):
    def __init__(self):
        super(WeatherSensor, self).__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(100,  100,  1720,  880)
        self.setWindowTitle('WS800')
        self.setWindowIcon(QIcon('./images/WS800.ico'))
        self.Tem = pg.PlotWidget()
        self.Tem.setLabel("left","Temperature [°C]")
        self.Tem.setLabel("bottom","Measurement Time")
        # 背景色改为白色
        self.Tem.setBackground('w')
        # 这样只重新plot该曲线，性能更高
        self.curveTem = self.Tem.getPlotItem().plot(
            pen=pg.mkPen('r', width=2)
        )
        self.Hum = pg.PlotWidget()
        self.Hum.setLabel("left","RH [%]")
        self.Hum.setLabel("bottom","Measurement Time")
        # 背景色改为白色
        self.Hum.setBackground('w')
        # 这样只重新plot该曲线，性能更高
        self.curveHum = self.Hum.getPlotItem().plot(
            pen=pg.mkPen('b', width=2)
        )

        self.Radiation = pg.PlotWidget()
        self.Radiation.setLabel("left","Radation")
        self.Radiation.setLabel("bottom","Measurement Time")
        # 背景色改为白色
        self.Radiation.setBackground('w')
        # 这样只重新plot该曲线，性能更高
        self.curveRadiation = self.Radiation.getPlotItem().plot(
            pen=pg.mkPen('r', width=2)
        )
        self.i = 0
        self.x = [] # x轴的值
        self.y = [] # y轴的值

        # 启动定时器，每隔1秒通知刷新一次数据
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateData)
        self.timer.start(1000)
        # 创建其他Qt控件
        # 创建其他Qt控件
        okButton = QtWidgets.QPushButton("OK")
        lineEdit = QtWidgets.QLineEdit('点击信息')
        # 水平layout里面放 edit 和 button
        hbox = QtWidgets.QVBoxLayout()
        hbox.addWidget(lineEdit)
        hbox.addWidget(okButton)
        # 垂直layout里面放 pyqtgraph图表控件 和 前面的水平layout
        vbox = QtWidgets.QVBoxLayout()
        # vbox.addLayout(hbox)
        vbox.addWidget(self.Tem)
        vbox.addWidget(self.Hum)
        vbox.addWidget(self.Radiation)
        # vbox.addLayout(hbox)

        allbox = QtWidgets.QHBoxLayout()

        allbox.addLayout(hbox)
        allbox.addLayout(vbox)
        allbox.setStretch(0, 1)
        allbox.setStretch(1, 20)
        ## 设置间距为0
        allbox.setSpacing(0)


    # 设置全局layout
        self.setLayout(allbox)

    def updateData(self):
        self.i += 1
        if len(self.x)>20:
            self.x = self.x[1:]
            self.y = self.y[1:]
            self.x.append(self.i)
            # 创建随机温度值
            self.y.append(randint(10,30))
        else:
            self.x.append(self.i)
            # 创建随机温度值
            self.y.append(randint(10,30))


        # plot data: x, y values
        self.curveTem.setData(self.x,self.y)
        self.curveHum.setData(self.x,self.y)
        self.curveRadiation.setData(self.x,self.y)




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = WeatherSensor()
    main.show()
    app.exec_()