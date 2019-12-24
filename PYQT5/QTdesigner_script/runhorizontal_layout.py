import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from PYQT5.QTdesigner_script import horizontal_layout

if __name__ == '__main__':
    app = QApplication(sys.argv) #创建QApplication对象
    mainWindow = QMainWindow() #创建主窗口
    ui = horizontal_layout.Ui_MainWindow() #创建实例
    ui.setupUi(mainWindow) #向主窗口上添加控件
    mainWindow.show()
    sys.exit(app.exec_()) #进入主循环
