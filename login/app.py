import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKit import *
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

os.system('python web.py')
app = QApplication(sys.argv)

web = QWebView()
web.load(QUrl("https://pythonspot.com"))
web.show()

sys.exit(app.exec_())
