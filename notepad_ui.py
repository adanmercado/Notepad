# -*- coding: utf-8 -*-
from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Notepad(object):
    def setupUi(self, Notepad):
        Notepad.setObjectName("Notepad")
        Notepad.resize(656, 469)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconos/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Notepad.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(Notepad)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textContent = QtWidgets.QTextEdit(self.centralWidget)
        self.textContent.setTabStopWidth(40)
        self.textContent.setObjectName("textContent")
        self.verticalLayout.addWidget(self.textContent)
        Notepad.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar()
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 656, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        Notepad.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(Notepad)
        self.mainToolBar.setMovable(False)
        self.mainToolBar.setObjectName("mainToolBar")
        Notepad.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(Notepad)
        self.statusBar.setObjectName("statusBar")
        Notepad.setStatusBar(self.statusBar)
        self.actionOpenFile = QtWidgets.QAction(Notepad)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpenFile.setIcon(icon1)
        self.actionOpenFile.setShortcutVisibleInContextMenu(True)
        self.actionOpenFile.setObjectName("actionOpenFile")
        self.actionSave = QtWidgets.QAction(Notepad)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName("actionSave")
        self.actionSaveAs = QtWidgets.QAction(Notepad)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/save-as.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveAs.setIcon(icon3)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionExportToPdf = QtWidgets.QAction(Notepad)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/pdf-export.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExportToPdf.setIcon(icon4)
        self.actionExportToPdf.setObjectName("actionExportToPdf")
        self.actionExit = QtWidgets.QAction(Notepad)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon5)
        self.actionExit.setShortcutVisibleInContextMenu(True)
        self.actionExit.setObjectName("actionExit")
        self.actionCopy = QtWidgets.QAction(Notepad)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon6)
        self.actionCopy.setObjectName("actionCopy")
        self.actionCut = QtWidgets.QAction(Notepad)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon7)
        self.actionCut.setObjectName("actionCut")
        self.actionPaste = QtWidgets.QAction(Notepad)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon8)
        self.actionPaste.setObjectName("actionPaste")
        self.actionAbout = QtWidgets.QAction(Notepad)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon9)
        self.actionAbout.setObjectName("actionAbout")
        self.actionFullscreen = QtWidgets.QAction(Notepad)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/fullscreen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFullscreen.setIcon(icon10)
        self.actionFullscreen.setObjectName("actionFullscreen")
        self.actionSettings = QtWidgets.QAction(Notepad)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon11)
        self.actionSettings.setObjectName("actionSettings")
        self.actionCloseFile = QtWidgets.QAction(Notepad)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/close-file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCloseFile.setIcon(icon12)
        self.actionCloseFile.setObjectName("actionCloseFile")
        self.actionAboutQt = QtWidgets.QAction(Notepad)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/qt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAboutQt.setIcon(icon13)
        self.actionAboutQt.setObjectName("actionAboutQt")
        self.menuFile.addAction(self.actionOpenFile)
        self.menuFile.addAction(self.actionCloseFile)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addAction(self.actionExportToPdf)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAboutQt)
        self.menuHelp.addAction(self.actionSettings)
        self.menuView.addAction(self.actionFullscreen)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.mainToolBar.addAction(self.actionOpenFile)
        self.mainToolBar.addAction(self.actionCloseFile)
        self.mainToolBar.addAction(self.actionSave)
        self.mainToolBar.addAction(self.actionSaveAs)
        self.mainToolBar.addAction(self.actionExportToPdf)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionCopy)
        self.mainToolBar.addAction(self.actionCut)
        self.mainToolBar.addAction(self.actionPaste)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionFullscreen)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionAbout)
        self.mainToolBar.addAction(self.actionSettings)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionExit)

        self.retranslateUi(Notepad)
        QtCore.QMetaObject.connectSlotsByName(Notepad)

    def retranslateUi(self, Notepad):
        Notepad.setWindowTitle(QtWidgets.QApplication.translate("Notepad", "Notepad", None, -1))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("Notepad", "Archivo", None, -1))
        self.menuEdit.setTitle(QtWidgets.QApplication.translate("Notepad", "Editar", None, -1))
        self.menuHelp.setTitle(QtWidgets.QApplication.translate("Notepad", "Ayuda", None, -1))
        self.menuView.setTitle(QtWidgets.QApplication.translate("Notepad", "Ver", None, -1))
        self.mainToolBar.setWindowTitle(QtWidgets.QApplication.translate("Notepad", "Herramientas", None, -1))
        self.actionOpenFile.setText(QtWidgets.QApplication.translate("Notepad", "Abrir", None, -1))
        self.actionOpenFile.setShortcut(QtWidgets.QApplication.translate("Notepad", "Ctrl+O", None, -1))
        self.actionSave.setText(QtWidgets.QApplication.translate("Notepad", "Guardar", None, -1))
        self.actionSave.setShortcut(QtWidgets.QApplication.translate("Notepad", "Ctrl+G", None, -1))
        self.actionSaveAs.setText(QtWidgets.QApplication.translate("Notepad", "Guardar como", None, -1))
        self.actionSaveAs.setShortcut(QtWidgets.QApplication.translate("Notepad", "Ctrl+Shift+G", None, -1))
        self.actionExportToPdf.setText(QtWidgets.QApplication.translate("Notepad", "Convertir a pdf", None, -1))
        self.actionExportToPdf.setShortcut(QtWidgets.QApplication.translate("Notepad", "Ctrl+P", None, -1))
        self.actionExit.setText(QtWidgets.QApplication.translate("Notepad", "Salir", None, -1))
        self.actionExit.setShortcut(QtWidgets.QApplication.translate("Notepad", "Ctrl+Q", None, -1))
        self.actionCopy.setText(QtWidgets.QApplication.translate("Notepad", "Copiar", None, -1))
        self.actionCopy.setShortcut(QtWidgets.QApplication.translate("Notepad", "Ctrl+C", None, -1))
        self.actionCut.setText(QtWidgets.QApplication.translate("Notepad", "Cortar", None, -1))
        self.actionCut.setShortcut(QtWidgets.QApplication.translate("Notepad", "Ctrl+X", None, -1))
        self.actionPaste.setText(QtWidgets.QApplication.translate("Notepad", "Pegar", None, -1))
        self.actionPaste.setShortcut(QtWidgets.QApplication.translate("Notepad", "Ctrl+V", None, -1))
        self.actionAbout.setText(QtWidgets.QApplication.translate("Notepad", "Acerca de", None, -1))
        self.actionAbout.setShortcut(QtWidgets.QApplication.translate("Notepad", "F1", None, -1))
        self.actionFullscreen.setText(QtWidgets.QApplication.translate("Notepad", "Pantalla completa", None, -1))
        self.actionSettings.setText(QtWidgets.QApplication.translate("Notepad", "Configuracion", None, -1))
        self.actionCloseFile.setText(QtWidgets.QApplication.translate("Notepad", "Cerrar", None, -1))
        self.actionAboutQt.setText(QtWidgets.QApplication.translate("Notepad", "Acerca de Qt", None, -1))

from icons import icons
