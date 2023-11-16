# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DarazWishlist.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTextEdit,
    QVBoxLayout, QWidget)
# import rc_resource

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(770, 800)
        MainWindow.setMaximumSize(QSize(770, 800))
        icon = QIcon()
        icon.addFile(u":/images/resource/image/mansaranna.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QLineEdit{\n"
"	padding:10px;\n"
"	\n"
"	background-color: rgba(255, 255, 255, 100);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        MainWindow.setIconSize(QSize(0, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFrameShape(QFrame.StyledPanel)
        self.stackedWidget.setFrameShadow(QFrame.Raised)
        self.mainPage = QWidget()
        self.mainPage.setObjectName(u"mainPage")
        self.mainPage.setStyleSheet(u"#mainPage{\n"
"	\n"
"	border-image: url(:/images/resource/image/mansaranna.png);\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.mainPage)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, -1)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.loginBtn = QPushButton(self.mainPage)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setMinimumSize(QSize(0, 58))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.loginBtn.setFont(font)
        self.loginBtn.setStyleSheet(u"*{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"	padding:8px;\n"
"	background-color: rgba(255, 255, 255, 100);\n"
"	border-radius:25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	padding:8px;\n"
"	\n"
"	background-color: rgb(42, 42, 42);\n"
"	border-radius:25px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/images/darazLogo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.loginBtn.setIcon(icon1)
        self.loginBtn.setIconSize(QSize(100, 60))

        self.verticalLayout_3.addWidget(self.loginBtn)

        self.stackedWidget.addWidget(self.mainPage)
        self.wishlistPage = QWidget()
        self.wishlistPage.setObjectName(u"wishlistPage")
        self.wishlistPage.setStyleSheet(u"#wishlistPage{\n"
"	background-color: rgb(71, 71, 71);\n"
"}\n"
"QPushButton{\n"
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
        self.gridLayout = QGridLayout(self.wishlistPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.wishlistPage)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.back1Btn = QPushButton(self.frame)
        self.back1Btn.setObjectName(u"back1Btn")
        self.back1Btn.setStyleSheet(u"QPushButton{\n"
"	padding:5px;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 255, 255, 100);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/resource/icon/chevron-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.back1Btn.setIcon(icon2)

        self.gridLayout_2.addWidget(self.back1Btn, 0, 0, 1, 1, Qt.AlignLeft)

        self.settingBtn = QPushButton(self.frame)
        self.settingBtn.setObjectName(u"settingBtn")
        self.settingBtn.setStyleSheet(u"QPushButton{\n"
"	padding:10px;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-radius:25px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 255, 255, 100);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/resource/icon/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingBtn.setIcon(icon3)
        self.settingBtn.setIconSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.settingBtn, 2, 2, 1, 1, Qt.AlignRight)

        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")
        font1 = QFont()
        font1.setPointSize(12)
        self.textEdit.setFont(font1)
        self.textEdit.setStyleSheet(u"#textEdit{\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius:25px;\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.gridLayout_2.addWidget(self.textEdit, 1, 0, 1, 3)

        self.addWishListBtn = QPushButton(self.frame)
        self.addWishListBtn.setObjectName(u"addWishListBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addWishListBtn.sizePolicy().hasHeightForWidth())
        self.addWishListBtn.setSizePolicy(sizePolicy)
        self.addWishListBtn.setFont(font1)
        self.addWishListBtn.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/images/resource/image/wishlist.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addWishListBtn.setIcon(icon4)
        self.addWishListBtn.setIconSize(QSize(36, 36))

        self.gridLayout_2.addWidget(self.addWishListBtn, 2, 0, 1, 1)

        self.addWishListStopBtn = QPushButton(self.frame)
        self.addWishListStopBtn.setObjectName(u"addWishListStopBtn")
        sizePolicy.setHeightForWidth(self.addWishListStopBtn.sizePolicy().hasHeightForWidth())
        self.addWishListStopBtn.setSizePolicy(sizePolicy)
        self.addWishListStopBtn.setMinimumSize(QSize(434, 52))
        self.addWishListStopBtn.setFont(font1)
        self.addWishListStopBtn.setStyleSheet(u"background-color: rgba(255, 82, 82,200);")
        self.addWishListStopBtn.setIconSize(QSize(36, 36))

        self.gridLayout_2.addWidget(self.addWishListStopBtn, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.wishlistPage)
        self.settingPage = QWidget()
        self.settingPage.setObjectName(u"settingPage")
        self.settingPage.setStyleSheet(u"#settingPage{\n"
"		background-color: rgb(71, 71, 71);\n"
"}")
        self.gridLayout_3 = QGridLayout(self.settingPage)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.back2Btn = QPushButton(self.settingPage)
        self.back2Btn.setObjectName(u"back2Btn")
        self.back2Btn.setStyleSheet(u"QPushButton{\n"
"	padding:5px;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 255, 255, 100);\n"
"}")
        self.back2Btn.setIcon(icon2)

        self.horizontalLayout.addWidget(self.back2Btn, 0, Qt.AlignLeft)


        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.label_3 = QLabel(self.settingPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 600))
        self.label_3.setMaximumSize(QSize(746, 630))
        self.label_3.setTextFormat(Qt.AutoText)
        self.label_3.setPixmap(QPixmap(u":/images/resource/image/help.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setWordWrap(False)

        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 3)

        self.wishlistIDSaveBtn = QPushButton(self.settingPage)
        self.wishlistIDSaveBtn.setObjectName(u"wishlistIDSaveBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.wishlistIDSaveBtn.sizePolicy().hasHeightForWidth())
        self.wishlistIDSaveBtn.setSizePolicy(sizePolicy1)
        self.wishlistIDSaveBtn.setMinimumSize(QSize(150, 0))
        self.wishlistIDSaveBtn.setFont(font1)
        self.wishlistIDSaveBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(93, 255, 112);\n"
"	color: rgb(0, 0, 0);\n"
"	padding:5px;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(71, 255, 30);\n"
"}")

        self.gridLayout_3.addWidget(self.wishlistIDSaveBtn, 1, 2, 1, 1)

        self.label_2 = QLabel(self.settingPage)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_wishlistID = QLineEdit(self.settingPage)
        self.lineEdit_wishlistID.setObjectName(u"lineEdit_wishlistID")
        self.lineEdit_wishlistID.setFont(font1)

        self.gridLayout_3.addWidget(self.lineEdit_wishlistID, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.settingPage)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 10))
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.addWishListBtn.clicked.connect(self.addWishListStopBtn.show)
        self.addWishListStopBtn.clicked.connect(self.addWishListBtn.show)
        self.addWishListStopBtn.clicked.connect(self.addWishListStopBtn.hide)
        self.addWishListBtn.clicked.connect(self.addWishListBtn.hide)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Daraz Wishlist", None))
        self.loginBtn.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.back1Btn.setText("")
        self.settingBtn.setText("")
        self.addWishListBtn.setText(QCoreApplication.translate("MainWindow", u"ADD to Wishlist", None))
        self.addWishListStopBtn.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.back2Btn.setText("")
        self.label_3.setText("")
        self.wishlistIDSaveBtn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Wishlist Button\n"
" ID", None))
        self.lineEdit_wishlistID.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex: block-CATyli37LyV", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"All Right Reserved @ 2023", None))
    # retranslateUi

