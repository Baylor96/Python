import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QDesktopWidget
from PyQt5.QtGui import QIcon

class CenterForm(QMainWindow):
    def __init__(self):
        super(CenterForm,self).__init__()
        self.setWindowTitle('主窗口居中应用')
        self.resize(400,300)
        self.status = self.statusBar()
        self.status.showMessage('只存在5秒的消息',5000)

    def center(self):
        #获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        #获取窗口坐标系
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.width()) / 2
        self.move(newLeft,newTop)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./Images/cartoon2.ico'))
    main = CenterForm()
    main.show()
    sys.exit(app.exec_())