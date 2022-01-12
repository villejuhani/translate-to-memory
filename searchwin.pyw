"""
@author: Ville Hytönen
@version: 11.1.2022
@state: In Development
"""
from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser


# GUI with functions, search a word from sanakirja.org with some language options
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(301, 128)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(20, 10, 181, 21))
        self.label1.setObjectName("label1")

        #label2 for testing reasons while in development
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(20, 50, 181, 21))
        self.label2.setObjectName("label2")



        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(210, 60, 75, 23))
        self.button1.setObjectName("button1")
        self.searchbar = QtWidgets.QLineEdit(self.centralwidget)
        self.searchbar.setGeometry(QtCore.QRect(20, 30, 261, 20))
        self.searchbar.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.searchbar.setText("")
        self.searchbar.setObjectName("searchbar")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(140, 60, 51, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 301, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.button1.clicked.connect(lambda: self.clickSearch("sörchd"))
        self.comboBox.currentIndexChanged.connect(self.langChange)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Translate to Memory"))
        self.label1.setText(_translate("MainWindow", "Translate a word using sanakirja.org"))
        self.label2.setText(_translate("MainWindow", "en - fi"))
        self.button1.setText(_translate("MainWindow", "Search"))
        self.button1.setShortcut(_translate("MainWindow", "Return"))
        self.comboBox.setItemText(0, _translate("MainWindow", "en - fi"))
        self.comboBox.setItemText(1, _translate("MainWindow", "fi - en"))
        self.comboBox.setItemText(2, _translate("MainWindow", "sv - fi"))
        self.comboBox.setItemText(3, _translate("MainWindow", "fi - sv"))
        self.comboBox.setItemText(4, _translate("MainWindow", "de - fi"))
        self.comboBox.setItemText(5, _translate("MainWindow", "fi - de"))


    # Function for clicking "search" button or pressing enter
    # Creates and searches an url based on what is the current text on the GUI searchbar
    # @param text ,text from searchbar  
    def clickSearch(self, text):
        word = self.searchbar.text()
        self.label1.setText(word + " " + text) # visual testing, changes label, delete later
        
        base_url = "https://www.sanakirja.org/search.php?q="

        

        langs = self.comboBox.currentText()
        lang_num = self.checkLang(langs)
        source_lang = "&l=" + lang_num[0]
        target_lang = "&l2=" + lang_num[1]

        webbrowser.open_new_tab(base_url + word + source_lang + target_lang)


    # Changes a label on GUI when search language is changed
    def langChange(self):
        langs = self.comboBox.currentText()
        self.label2.setText(langs)

    
    # Interprets combobox languages
    # Returns array of corresponding numbers(string) for chosen languages
    # @param langs current text in language choice combobox
    # @return array of corresponding numbers(string) for chosen languages
    def checkLang(self, langs):

        #combobox text is in form of "aa - bb"
        source_lang = langs[0] + langs[1]
        target_lang = langs[5] + langs[6]

        # language and corresponding number used in sanakirja.org url
        refLangs = [ ["fi", "17"], ["en", "3"], ["sv","15"], ["de", "16"] ]

        lang_num = []

        for i in range(len(refLangs)):
            if source_lang == refLangs[i][0]:
                source_lang = refLangs [i][1]
                lang_num.append(source_lang)
        
        for i in range(len(refLangs)):
            if target_lang == refLangs[i][0]:
                target_lang = refLangs[i][1]
                lang_num.append(target_lang)

        return lang_num       


# Starts GUI
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
