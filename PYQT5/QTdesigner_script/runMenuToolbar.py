import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from PYQT5.QTdesigner_script import MenuToolbar

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = MenuToolbar.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())