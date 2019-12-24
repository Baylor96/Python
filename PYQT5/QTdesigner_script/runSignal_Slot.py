import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from PYQT5.QTdesigner_script import Signal_Slot

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Signal_Slot.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())