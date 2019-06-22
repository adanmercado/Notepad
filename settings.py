# -*- coding: utf-8 -*-
from PySide2.QtWidgets import QDialog
from PySide2.QtCore import QSettings
from settings_ui import Ui_Settings

class NotepadSettings(Ui_Settings, QDialog):
	def __init__(self):
		super(NotepadSettings, self).__init__()
		self.setupUi(self)

		self.btnCancel.clicked.connect(self.reject)
		self.btnSave.clicked.connect(self.saveSettings)

		settings = QSettings()
		font = settings.value('Notepad/Font', 'Roboto')
		fontSize = settings.value('Notepad/FontSize', 12.0)
		tabSpace = settings.value('Notepad/TabSpace', 40)

		self.comboFont.setCurrentFont(font)
		self.spinFontSize.setValue(fontSize)
		self.spinTab.setValue(tabSpace / 10)

	def saveSettings(self):
		font = self.comboFont.currentFont()
		fontSize = self.spinFontSize.value()
		tabSpace = self.spinTab.value() * 10

		settings = QSettings()
		settings.setValue('Notepad/Font', font)
		settings.setValue('Notepad/FontSize', fontSize)
		settings.setValue('Notepad/TabSpace', tabSpace)

		self.accept()