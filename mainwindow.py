# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtTest import QTest
from __Interface__.rc_resource import *
from __Interface__.ui_DarazWishlist import Ui_MainWindow as mainWindowUI
from darazWishListClick import darazWishListClick
import time
from threading import Thread


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.mainWindow = mainWindowUI()
        self.mainWindow.setupUi(self)
        self.stop = False
        self.loginTask = Thread(target=self.login)
        self.addToWishlistTask = Thread(target=self.addToWishlist)
        self.mainWindow.loginBtn.clicked.connect(lambda: self.loginTask.start())
        self.mainWindow.addWishListBtn.clicked.connect(
            lambda: self.addToWishlistTask.start()
        )
        self.mainWindow.back1Btn.clicked.connect(self.back1Btn_clicked)
        self.mainWindow.settingBtn.clicked.connect(self.settingBtn_clicked)
        self.mainWindow.wishlistIDSaveBtn.clicked.connect(
            self.wishlistIDSaveBtn_clicked
        )
        self.mainWindow.back2Btn.clicked.connect(self.back2Btn_clicked)
        self.mainWindow.addWishListStopBtn.hide()
        self.mainWindow.addWishListStopBtn.clicked.connect(self.stopThread)
        self.show()

    def stopThread(self):
        self.stop = True

    def closeEvent(self, event) -> None:
        self.stop = True
        return super().closeEvent(event)

    def back1Btn_clicked(self):
        self.mainWindow.stackedWidget.setCurrentIndex(0)

    def back2Btn_clicked(self):
        self.mainWindow.stackedWidget.setCurrentIndex(1)

    def settingBtn_clicked(self):
        self.mainWindow.stackedWidget.setCurrentIndex(2)

    def wishlistIDSaveBtn_clicked(self):
        id = self.mainWindow.lineEdit_wishlistID.text()
        if id == "":
            return
        file = open("settings.txt", "w")
        file.write(id)
        file.close()
        self.mainWindow.lineEdit_wishlistID.setStyleSheet(
            "background-color: rgb(93, 255, 112)"
        )
        QTest.qWait(100)
        self.mainWindow.lineEdit_wishlistID.setStyleSheet(
            "background-color: rgba(255, 255, 255, 100)"
        )

    def login(self):
        self.daraz_wish_list_click = darazWishListClick()
        loginLink = "https://member.daraz.lk/user/login"
        self.daraz_wish_list_click.openNewLink(loginLink)
        try:
            self.daraz_wish_list_click.loin()
        except:
            pass
        self.addToWishListPage()

    def addToWishListPage(self):
        self.mainWindow.stackedWidget.setCurrentIndex(1)

    def addToWishlist(self):
        self.loginTask.join()
        errorLink = []
        file_links = self.mainWindow.textEdit.toPlainText()
        links = file_links.split("\n")
        for link in links:
            if self.stop == True:
                self.mainWindow.textEdit.setStyleSheet(
                    "background-color: rgba(255, 82, 80,200);"
                )
                # break
                return
            link = link.strip()
            try:
                self.daraz_wish_list_click.openNewLink(link)
                self.daraz_wish_list_click.clickWishListBtn()
            except:
                errorLink.append(link)
            time.sleep(1)
        self.mainWindow.textEdit.setStyleSheet(
            "background-color: rgba(160, 255, 83,150)"
        )

        if len(errorLink) > 0:
            errorFile = open("error links.txt", "w")
            for errlink in errorLink:
                errorFile.write(errlink)

            errorFile.close()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
