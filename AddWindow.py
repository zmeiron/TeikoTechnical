# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddWindow.ui'
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
        MainWindow.resize(391, 494)
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
        self.label_13 = QLabel(self.centralWidget)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 12, 0, 1, 1)

        self.responseLineEdit = QLineEdit(self.centralWidget)
        self.responseLineEdit.setObjectName(u"responseLineEdit")

        self.gridLayout.addWidget(self.responseLineEdit, 6, 1, 1, 1)

        self.label_14 = QLabel(self.centralWidget)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 13, 0, 1, 1)

        self.label_2 = QLabel(self.centralWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_12 = QLabel(self.centralWidget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 11, 0, 1, 1)

        self.label_7 = QLabel(self.centralWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.sampleLineEdit = QLineEdit(self.centralWidget)
        self.sampleLineEdit.setObjectName(u"sampleLineEdit")

        self.gridLayout.addWidget(self.sampleLineEdit, 7, 1, 1, 1)

        self.sampleTypeLineEdit = QLineEdit(self.centralWidget)
        self.sampleTypeLineEdit.setObjectName(u"sampleTypeLineEdit")

        self.gridLayout.addWidget(self.sampleTypeLineEdit, 8, 1, 1, 1)

        self.label_9 = QLabel(self.centralWidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)

        self.label_6 = QLabel(self.centralWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.label_8 = QLabel(self.centralWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)

        self.label_11 = QLabel(self.centralWidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 10, 0, 1, 1)

        self.sexLineEdit = QLineEdit(self.centralWidget)
        self.sexLineEdit.setObjectName(u"sexLineEdit")

        self.gridLayout.addWidget(self.sexLineEdit, 4, 1, 1, 1)

        self.conditionLineEdit = QLineEdit(self.centralWidget)
        self.conditionLineEdit.setObjectName(u"conditionLineEdit")

        self.gridLayout.addWidget(self.conditionLineEdit, 2, 1, 1, 1)

        self.ageLineEdit = QLineEdit(self.centralWidget)
        self.ageLineEdit.setObjectName(u"ageLineEdit")

        self.gridLayout.addWidget(self.ageLineEdit, 3, 1, 1, 1)

        self.projectLineEdit = QLineEdit(self.centralWidget)
        self.projectLineEdit.setObjectName(u"projectLineEdit")

        self.gridLayout.addWidget(self.projectLineEdit, 0, 1, 1, 1)

        self.tftLineEdit = QLineEdit(self.centralWidget)
        self.tftLineEdit.setObjectName(u"tftLineEdit")

        self.gridLayout.addWidget(self.tftLineEdit, 9, 1, 1, 1)

        self.subjectLineEdit = QLineEdit(self.centralWidget)
        self.subjectLineEdit.setObjectName(u"subjectLineEdit")

        self.gridLayout.addWidget(self.subjectLineEdit, 1, 1, 1, 1)

        self.label_5 = QLabel(self.centralWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_10 = QLabel(self.centralWidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)

        self.label = QLabel(self.centralWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_4 = QLabel(self.centralWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.treatmentLineEdit = QLineEdit(self.centralWidget)
        self.treatmentLineEdit.setObjectName(u"treatmentLineEdit")

        self.gridLayout.addWidget(self.treatmentLineEdit, 5, 1, 1, 1)

        self.label_3 = QLabel(self.centralWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_15 = QLabel(self.centralWidget)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 14, 0, 1, 1)

        self.bLineEdit = QLineEdit(self.centralWidget)
        self.bLineEdit.setObjectName(u"bLineEdit")

        self.gridLayout.addWidget(self.bLineEdit, 10, 1, 1, 1)

        self.cd8LineEdit = QLineEdit(self.centralWidget)
        self.cd8LineEdit.setObjectName(u"cd8LineEdit")

        self.gridLayout.addWidget(self.cd8LineEdit, 11, 1, 1, 1)

        self.cd4LineEdit = QLineEdit(self.centralWidget)
        self.cd4LineEdit.setObjectName(u"cd4LineEdit")

        self.gridLayout.addWidget(self.cd4LineEdit, 12, 1, 1, 1)

        self.nkLineEdit = QLineEdit(self.centralWidget)
        self.nkLineEdit.setObjectName(u"nkLineEdit")

        self.gridLayout.addWidget(self.nkLineEdit, 13, 1, 1, 1)

        self.monoLineEdit = QLineEdit(self.centralWidget)
        self.monoLineEdit.setObjectName(u"monoLineEdit")

        self.gridLayout.addWidget(self.monoLineEdit, 14, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.addButton = QPushButton(self.centralWidget)
        self.addButton.setObjectName(u"addButton")

        self.verticalLayout.addWidget(self.addButton)

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
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"cd4_t_cell count", None))
#if QT_CONFIG(tooltip)
        self.responseLineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"Did the subject respond to the treatment?", None))
#endif // QT_CONFIG(tooltip)
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"nk_cell count", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("MainWindow", u"Which subject is the sample from?", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Subject", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"cd8_t_cell count", None))
#if QT_CONFIG(tooltip)
        self.label_7.setToolTip(QCoreApplication.translate("MainWindow", u"Did the subject respond to the treatment?", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Response", None))
#if QT_CONFIG(tooltip)
        self.sampleLineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"What sample is it? (s##)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.sampleTypeLineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"What is the sample type?", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_9.setToolTip(QCoreApplication.translate("MainWindow", u"What is the sample type?", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Sample Type", None))
#if QT_CONFIG(tooltip)
        self.label_6.setToolTip(QCoreApplication.translate("MainWindow", u"What treatment is the subject recieving?", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Treatment", None))
#if QT_CONFIG(tooltip)
        self.label_8.setToolTip(QCoreApplication.translate("MainWindow", u"What sample is it? (s##)", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Sample", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"b_cell count", None))
#if QT_CONFIG(tooltip)
        self.sexLineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"What is the subject's sex?", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.conditionLineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"What is the subject's condition?", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.ageLineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"What is the subject's age?", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.projectLineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"What project is the sample a part of?", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.tftLineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"Time since the treatment in days", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.subjectLineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"Which subject is the sample from?", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("MainWindow", u"What is the subject's sex?", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Sex", None))
#if QT_CONFIG(tooltip)
        self.label_10.setToolTip(QCoreApplication.translate("MainWindow", u"Time since the treatment in days", None))
#endif // QT_CONFIG(tooltip)
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Time From Treatment", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("MainWindow", u"What project is the sample a part of?", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Project", None))
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("MainWindow", u"What is the subject's age?", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Age", None))
#if QT_CONFIG(tooltip)
        self.treatmentLineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"What treatment is the subject recieving?", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("MainWindow", u"What is the subject's condition?", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Condition", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"monocyte count", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"Add Sample", None))
    # retranslateUi

