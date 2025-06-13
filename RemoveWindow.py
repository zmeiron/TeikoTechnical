# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RemoveWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(192, 92)
        self.open_file_action = QAction(MainWindow)
        self.open_file_action.setObjectName(u"open_file_action")
        self.actionAdd_Sample = QAction(MainWindow)
        self.actionAdd_Sample.setObjectName(u"actionAdd_Sample")
        self.actionRemove_Sample = QAction(MainWindow)
        self.actionRemove_Sample.setObjectName(u"actionRemove_Sample")
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.centralWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.sampleLineEdit = QLineEdit(self.centralWidget)
        self.sampleLineEdit.setObjectName(u"sampleLineEdit")

        self.gridLayout.addWidget(self.sampleLineEdit, 0, 1, 1, 1)

        self.label_8 = QLabel(self.centralWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.removeButton = QPushButton(self.centralWidget)
        self.removeButton.setObjectName(u"removeButton")

        self.verticalLayout.addWidget(self.removeButton)

        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Add a Sample", None))
        self.open_file_action.setText(QCoreApplication.translate("MainWindow", u"Open file...", None))
        self.actionAdd_Sample.setText(QCoreApplication.translate("MainWindow", u"Add Sample", None))
#if QT_CONFIG(tooltip)
        self.actionAdd_Sample.setToolTip(QCoreApplication.translate("MainWindow", u"Add a sample to the database", None))
#endif // QT_CONFIG(tooltip)
        self.actionRemove_Sample.setText(QCoreApplication.translate("MainWindow", u"Remove Sample", None))
#if QT_CONFIG(tooltip)
        self.actionRemove_Sample.setToolTip(QCoreApplication.translate("MainWindow", u"Remove a sample from the database", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.sampleLineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"What sample is it? (s##)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_8.setToolTip(QCoreApplication.translate("MainWindow", u"What sample is it? (s##)", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Sample to Remove", None))
        self.removeButton.setText(QCoreApplication.translate("MainWindow", u"Remove Sample", None))
    # retranslateUi

