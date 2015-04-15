Title: PyQt 创建新窗口
Date: 2015-04-15 19:36
Modified: 2015-04-15 19:36
Category: it
Tags: pyqt, python
Slug: pyqt_create_a_new_window
Author: caimaoy


>PyQt 如何新建一个窗口


```
# -*- coding: UTF-8 -*-

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class mainWindow(QWidget):
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)
        button = QPushButton(u'弹出新窗口', self)
        self.slavewindow = slaveWindow()
        self.connect(button, SIGNAL('clicked()'), self.slavewindow.show)


class slaveWindow(QWidget):
    def __init__(self, parent = None):
        super(slaveWindow, self).__init__(parent)


def main():
    app = QApplication(sys.argv)
    mainwindow = mainWindow()
    mainwindow.show()
    app.exec_()


if __name__ == '__main__':
    main()
```
> 直接上代码

###备注

说说要注意的吧:

```
self.slavewindow = slaveWindow()
self.connect(button, SIGNAL('clicked()'), self.slavewindow.show)
```
- 这两个是关键
- 之前自己一个错误的做法是clicked信号关联了一个普通函数,在普通函数中创建新窗口的实例，同时调用show方法，现在想想实例的生命周期是有问题的，所以窗口一闪而过
