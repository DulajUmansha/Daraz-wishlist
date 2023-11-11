# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addLink.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)
import rc_resource

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(556, 793)
        icon = QIcon()
        icon.addFile(u":/icons/list.svg", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"#Form{\n"
"	background-image: url(:/images/resource/image/OIP.jpeg);\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"#textEdit{\n"
"	border-radius:25px;\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.verticalLayout_3.addWidget(self.textEdit)

        self.verticalSpacer = QSpacerItem(20, 16, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        font = QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	padding:8px;\n"
"		color: rgb(255, 255, 255);\n"
"	background-color: rgba(0, 0, 0, 100);\n"
"	border-radius:25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	padding:8px;\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 100);\n"
"	border-radius:25px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/images/resource/image/wishlist.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(36, 36))

        self.verticalLayout_3.addWidget(self.pushButton, 0, Qt.AlignHCenter)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	padding:5px;\n"
"	border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgba(255, 255, 255, 100);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/resource/icon/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.pushButton_2, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"WishList", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"ADD to Wishlist", None))
        self.pushButton_2.setText("")
    # retranslateUi

