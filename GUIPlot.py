# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 10:52:22 2021

@author: Hengheng Zhang

E-Mail: hengheng.zhang@kit.edu

Function：

"""
from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg
import sys
from random import randint

class MainWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('pyqtgraph作图示例')
        # 创建 PlotWidget 对象
        self.pw = pg.PlotWidget()

        # 设置图表标题
        # self.pw.setTitle("气温趋势",color='008080',size='12pt')

        # 设置上下左右的label
        self.pw.setLabel("left","Temperature [°C]")
        self.pw.setLabel("bottom","Measurement Time")
        # 背景色改为白色
        self.pw.setBackground('w')
        # self.pw.setYRange(min=-10, # 最小值
        #                   max=50)  # 最大值
        # self.setCentralWidget(self.pw)
        # 实时显示应该获取 plotItem， 调用setData，
        # 这样只重新plot该曲线，性能更高
        self.curve = self.pw.getPlotItem().plot(
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
        okButton = QtWidgets.QPushButton("OK")
        lineEdit = QtWidgets.QLineEdit('点击信息')
        # 水平layout里面放 edit 和 button
        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(lineEdit)
        hbox.addWidget(okButton)
        # 垂直layout里面放 pyqtgraph图表控件 和 前面的水平layout
        vbox = QtWidgets.QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.pw)
        # 设置全局layout
        self.setLayout(vbox)

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
        self.curve.setData(self.x,self.y)




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    app.exec_()