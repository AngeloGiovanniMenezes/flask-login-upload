from PySide.QtWebKit import *
from PySide.QtGui import *
from PySide.QtCore import *
import sys
import os

os.system("python web.py")
app = QApplication(sys.argv)
web = QWebView()
web.setUrl(QUrl("https://www.google.com"))
web.show()
sys.exit(app.exec_())
