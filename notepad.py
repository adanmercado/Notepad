# -*- coding: utf-8 -*-
from PySide2.QtWidgets import QMainWindow, QMessageBox, QDialog, QFileDialog, QTextEdit
from PySide2.QtCore import QFile, QDir, QIODevice, QTextStream, QSettings
from PySide2.QtGui import QCloseEvent, QWindow
from PySide2.QtPrintSupport import QPrinter

from notepad_ui import Ui_Notepad
from settings import NotepadSettings

class Notepad(Ui_Notepad, QMainWindow):
	def __init__(self):
		super(Notepad, self).__init__()
		self.setupUi(self)
		self.doConnections()
		self.loadSettings()
		self.filename = ''
		self.fileFilter = 'Archivos (*.txt *.cpp *.c *.h *.py *.sh)'

	def doConnections(self):
		self.actionExit.triggered.connect(self.close)
		self.actionOpenFile.triggered.connect(self.openFile)
		self.actionCloseFile.triggered.connect(self.closeFile)
		self.actionSave.triggered.connect(self.saveFile)
		self.actionSaveAs.triggered.connect(self.saveFileAs)
		self.actionExportToPdf.triggered.connect(self.exportToPdf)
		self.actionCopy.triggered.connect(self.textContent.copy)
		self.actionPaste.triggered.connect(self.textContent.paste)
		self.actionCut.triggered.connect(self.textContent.cut)
		self.actionFullscreen.triggered.connect(self.fullscreen)
		self.actionAbout.triggered.connect(self.about)
		self.actionAboutQt.triggered.connect(self.aboutQt)
		self.actionSettings.triggered.connect(self.settings)

	def closeEvent(self, event):
		if self.filename:
			exit = QMessageBox().question(self, 'Archivo en uso', '<p>Actualmente se encuentra abierto el archivo {}, '
				'todos los cambios se perderán.<br>¿Deseas continuar?</p>'.format(self.filename), QMessageBox.Cancel | QMessageBox.Ok)

			if exit == QMessageBox.Cancel: 
				event.ignore()
				return
		else: 
			data = self.textContent.toPlainText()
			if data:
				exit = QMessageBox().question(self, 'Contenido modificado', '<p>El contenido modificado no ha sido guardado '
					'en ningún archivo, todos los cambios se perderán.<br>¿Deseas continuar?</p>', QMessageBox.Cancel | QMessageBox.Ok)

				if exit == QMessageBox.Cancel: 
					event.ignore()
					return
		
		event.accept()

	def showMessage(self, str):
		self.statusBar.showMessage(str, 3000)

	def openFile(self):
		dir = QDir()
		docsPath = '{}/Documents'.format(dir.homePath())
		if not dir.exists(docsPath): docsPath = '{}/Documentos'.format(dir.homePath())
		
		#Regresa una tupla (filename, filter)
		filename = QFileDialog.getOpenFileName(self, 'Abrir', docsPath, self.fileFilter)
		if not filename: return

		self.filename = filename[0]

		file = QFile(self.filename)
		if not file.open(QIODevice.ReadOnly): return

		data = file.readAll()
		file.close()

		self.textContent.clear()
		self.textContent.setText(str(data, encoding='utf-8'))
		self.setWindowTitle('{} - {}'.format(self.windowTitle(), self.filename))

	def closeFile(self):
		if not self.filename: return

		self.textContent.clear()
		windowTitle = self.windowTitle().split('-')[0]
		self.setWindowTitle(windowTitle)
		self.filename = ''

	def saveFile(self):
		if not self.filename:
			self.saveFileAs()
			return

		file = QFile(self.filename)
		if not file.open(QIODevice.WriteOnly): return
		
		data = self.textContent.toPlainText()
		
		stream = QTextStream(file)
		stream.setCodec('UTF-8')
		stream << data;
		
		file.flush()
		file.close()
		self.showMessage('Archivo guardado')

	def saveFileAs(self):
		dir = QDir()
		docsPath = '{}/Documents'.format(dir.homePath())
		if not dir.exists(docsPath): docsPath = '{}/Documentos'.format(dir.homePath())
			
		#Regresa una tupla (filename, filter)
		filename = QFileDialog.getSaveFileName(self, 'Guardar como', docsPath, self.fileFilter)
		if not filename: return

		if self.filename: 
			windowTitle = self.windowTitle().split('-')[0]
			self.setWindowTitle('{} - {}'.format(windowTitle, filename[0]))
		else: 
			self.setWindowTitle('{} - {}'.format(self.windowTitle(), filename[0]))
			
		self.filename = filename[0]

		file = QFile(self.filename)
		if not file.open(QIODevice.WriteOnly): return
		
		data = self.textContent.toPlainText()
		
		stream = QTextStream(file)
		stream.setCodec('UTF-8')
		stream << data;
		
		file.flush()
		file.close()
		self.showMessage('Archivo guardado')

	def exportToPdf(self):
		data = self.textContent.toPlainText()
		if not data: return

		dir = QDir()
		docsPath = '{}/Documents'.format(dir.homePath())
		if not dir.exists(docsPath): docsPath = '{}/Documentos'.format(dir.homePath())
			
		#Regresa una tupla (filename, filter)
		filename = QFileDialog.getSaveFileName(self, 'Exportar a pdf', docsPath, 'Archivo pdf *.pdf')
		if not filename: return

		filename = filename[0]
		if not '.pdf' in filename: filename += '.pdf'

		printer = QPrinter(QPrinter.HighResolution)
		printer.setPaperSize(QPrinter.Letter)
		printer.setPageMargins(2, 2, 2, 2, QPrinter.Millimeter)
		printer.setCreator('Notepad')
		printer.setPrintProgram('Notepad')
		printer.setOutputFormat(QPrinter.PdfFormat)
		printer.setOutputFileName(filename)
		self.textContent.print_(printer)
		self.showMessage('Pdf guardado: {}'.format(filename))

	def fullscreen(self):
		if not self.isFullScreen(): 
			self.menuBar.setHidden(True)
			self.showFullScreen()
		else:
			self.menuBar.setHidden(False)
			self.showMaximized()

	def about(self):
		QMessageBox().about(self, 'Acerca de Notepad', '<p align=center><b>Notepad 1.0.0</b><br>'
			'Adán Eliel Mercado Peralta<br><br>'
			'Iconos por <a href=www.iconos8.es>iconos8</a><br><br>'
			'Este programa está hecho únicamente con fines didácticos.</p>')

	def aboutQt(self):
		QMessageBox().aboutQt(self, 'Acerca de Qt')

	def loadSettings(self):
		settings = QSettings()
		font = settings.value('Notepad/Font', 'Roboto')
		fontSize = settings.value('Notepad/FontSize', 12.0)
		font.setPointSize(fontSize)
		tabSpace = settings.value('Notepad/TabSpace', 40)
		self.textContent.setCurrentFont(font)
		self.textContent.setTabStopDistance(tabSpace)

	def settings(self):
		notepadSettings = NotepadSettings()
		if notepadSettings.exec_() == QDialog.Rejected: return

		cursor = self.textContent.textCursor()
		self.textContent.selectAll()
		self.loadSettings()
		self.textContent.setTextCursor(cursor)

