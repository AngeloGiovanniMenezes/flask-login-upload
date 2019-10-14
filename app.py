import sys
import os
from PySide import QtCore, QtGui, QtWebKit

#os.system('python web.py')

app = QtGui.QApplication(sys.argv)
view = QtWebKit.QWebView()
view.load(QtCore.QUrl('http://localhost:4000'))
view.show()

sys.exit(app.exec_())
