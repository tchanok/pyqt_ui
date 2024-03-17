import sys
from  PySide2.QtCore import Qt, QSize
from PySide2.QtWidgets import QMainWindow, QPushButton, QApplication
from PySide2.QtGui import QIcon
from interface import Ui_MainWindow
from ui_functions import UIFunctions

class MainWindow(QMainWindow):
    
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ##window//////////////////////////////////////////////////
        # frameless
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        #minimize
        self.ui.minimizeBtn.clicked.connect(lambda: self.showMinimized())

        # MAXIMIZE/RESTORE
        self.ui.restoreBtn.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # CLOSE APPLICATION
        self.ui.closeBtn.clicked.connect(lambda: self.close())
        
        #move window
        UIFunctions.uiDefinitions(self)

        #/////////////////////////////////////////////////////////


        ## TOGGLE  MENU
        self.ui.menuBtn.clicked.connect(lambda: UIFunctions.toggleMenu(self, 300, True))

        ##change stylesheet after clicked
        for widget in self.ui.leftMenuSubContainer.findChildren(QPushButton):
            widget.clicked.connect(self.clickedStyle)

        # Toggle left box
        #show menu
        self.ui.settingsBtn.clicked.connect(lambda: UIFunctions.toggleLeftBox(self, True))
        self.ui.infoBtn.clicked.connect(lambda: UIFunctions.toggleLeftBox(self, True))
        self.ui.helpBtn.clicked.connect(lambda: UIFunctions.toggleLeftBox(self, True))
        #hide menu
        self.ui.centerMenuCloseBtn.clicked.connect(lambda: UIFunctions.closeLeftBox(self, True))

        # Toggle right box
        #show menu
        self.ui.profileBtn.clicked.connect(lambda: UIFunctions.toggleRightBox(self, True))
        self.ui.profileBtn.clicked.connect(lambda: UIFunctions.changePage(self, "stackedWidget_2", 0))
        self.ui.moreBtn.clicked.connect(lambda: UIFunctions.toggleRightBox(self, True))
        self.ui.moreBtn.clicked.connect(lambda: UIFunctions.changePage(self, "stackedWidget_2", 1))
        #hide menu
        self.ui.rightMenuCloseBtn.clicked.connect(lambda: UIFunctions.closeRightBox(self, True))

        # noti box
        #show menu
        self.ui.NotiBtn.clicked.connect(lambda: UIFunctions.toggleNotiBox(self, True))
        #hide menu
        self.ui.notiCloseBtn.clicked.connect(lambda: UIFunctions.closeNotiBox(self, True))
        self.ui.popupNotificationContainer.setMinimumSize(QSize(600, 0))
        self.ui.popupNotificationContainer.setMaximumSize(QSize(600, 0))
        


    def clickedStyle(self):
        for widget in self.ui.leftMenuSubContainer.findChildren(QPushButton):
            btnName = self.sender().objectName()
            #set icons
            if btnName == "menuBtn":
                if widget.objectName() == "menuBtn" and self.ui.leftMenuContainer.width() == 60:
                    widget.setIcon(QIcon(u":/icons/icons/chevron-left.svg"))
                    menuState = 1
                if widget.objectName() == "menuBtn" and self.ui.leftMenuContainer.width() != 60:
                    widget.setIcon(QIcon(u":/icons/icons/align-justify.svg"))
                    menuState = 0

            else:
            
                #set icon's styleSheet
                clickedStyle = widget.styleSheet() + "background-color: #2c313c; border-left: 2px solid #3e3e42; border-bottom: 3px solid #3e3e42;"

                defaultStyle = ""

                if widget.objectName() != self.sender().objectName():
                
                    widget.setStyleSheet(defaultStyle)
                else:
                    widget.setStyleSheet(clickedStyle)


                if btnName == "homeBtn" or btnName == "dataBtn" or btnName == "reportBtn":
                    stackedWidgetName = "stackedWidget_3"
                    if btnName == "homeBtn":
                        pageIndex = 0
                    elif btnName == "dataBtn":
                        pageIndex = 1
                    elif btnName == "reportBtn":
                        pageIndex = 2
                elif btnName == "settingsBtn" or btnName == "infoBtn" or btnName == "helpBtn":
                    stackedWidgetName = "stackedWidget"
                    if btnName == "settingsBtn":
                        pageIndex = 0
                    elif btnName == "infoBtn":
                        pageIndex = 1
                    elif btnName == "helpBtn":
                        pageIndex = 2
            
        if btnName != "menuBtn":
            UIFunctions.changePage(self, stackedWidgetName, pageIndex)

        #SHOW WINDOW
        self.show()

    def mousePressEvent(self, event):
        #get the current position of the mouse
        self.dragPos = event.globalPos()

#Execute APP
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
