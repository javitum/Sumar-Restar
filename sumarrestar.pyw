import sys
from PyQt5 import QtWidgets
from sumarrestar import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
