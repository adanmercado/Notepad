# -*- coding: utf-8 -*-
import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QCoreApplication

from notepad import Notepad

if __name__ == '__main__':
	QCoreApplication.setOrganizationName('AdanMercado')
	QCoreApplication.setOrganizationDomain('https://github.com/adanmercado')
	QCoreApplication.setApplicationName('Notepad')
	QCoreApplication.setApplicationVersion('1.0.0')
	app = QApplication(sys.argv)

	notepad = Notepad()
	notepad.showMaximized()

	sys.exit(app.exec_())