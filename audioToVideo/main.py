import sys
from custome_errors import *
sys.excepthook = my_excepthook
import update
import gui
import guiTools
from settings import *
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
language.init_translation()
class main (qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(app.name + _("version : ") + str(app.version))
        layout=qt.QVBoxLayout()
        self.path=guiTools.QReadOnlyTextEdit()
        layout.addWidget(qt.QLabel(_("audio file")))
        layout.addWidget(self.path)
        self.selectFile=guiTools.QPushButton(_("select file"))
        self.selectFile.clicked.connect(self.on_select_file)
        layout.addWidget(self.selectFile)
        self.imagePath=guiTools.QReadOnlyTextEdit()
        layout.addWidget(qt.QLabel(_("image file")))
        layout.addWidget(self.imagePath)
        self.selectImageFile=guiTools.QPushButton(_("select file"))
        self.selectImageFile.clicked.connect(self.on_select_image_file)
        layout.addWidget(self.selectImageFile)
        self.outputDir=guiTools.QReadOnlyTextEdit()
        layout.addWidget(qt.QLabel(_("output folder")))
        layout.addWidget(self.outputDir)
        self.selectOutputDIR=guiTools.QPushButton(_("select folder"))
        self.selectOutputDIR.clicked.connect(self.on_select_output_folder)
        layout.addWidget(self.selectOutputDIR)
        self.startConvertion=guiTools.QPushButton(_("convert to video"))
        self.startConvertion.clicked.connect(lambda:gui.ConvertGUI(self,self.path.toPlainText(),self.outputDir.toPlainText(),self.imagePath.toPlainText()).exec())
        layout.addWidget(self.startConvertion)

        self.setting=guiTools.QPushButton(_("settings"))
        self.setting.clicked.connect(lambda: settings(self).exec())
        layout.addWidget(self.setting)
        w=qt.QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

        mb=self.menuBar()
        help=mb.addMenu(_("help"))
        helpFile=qt1.QAction(_("help file"),self)
        help.addAction(helpFile)
        helpFile.triggered.connect(lambda:guiTools.HelpFile())
        helpFile.setShortcut("f1")
        cus=help.addMenu(_("contact us"))
        telegram=qt1.QAction("telegram",self)
        cus.addAction(telegram)
        telegram.triggered.connect(lambda:guiTools.OpenLink(self,"https://t.me/mesteranasm"))
        telegramc=qt1.QAction(_("telegram channel"),self)
        cus.addAction(telegramc)
        telegramc.triggered.connect(lambda:guiTools.OpenLink(self,"https://t.me/tprogrammers"))
        githup=qt1.QAction(_("Github"),self)
        cus.addAction(githup)
        githup.triggered.connect(lambda: guiTools.OpenLink(self,"https://Github.com/mesteranas"))
        X=qt1.QAction(_("x"),self)
        cus.addAction(X)
        X.triggered.connect(lambda:guiTools.OpenLink(self,"https://x.com/mesteranasm"))
        email=qt1.QAction(_("email"),self)
        cus.addAction(email)
        email.triggered.connect(lambda: guiTools.sendEmail("anasformohammed@gmail.com","project_type=GUI app={} version={}".format(app.name,app.version),""))
        Github_project=qt1.QAction(_("visite project on Github"),self)
        help.addAction(Github_project)
        Github_project.triggered.connect(lambda:guiTools.OpenLink(self,"https://Github.com/mesteranas/{}".format(settings_handler.appName)))
        Checkupdate=qt1.QAction(_("check for update"),self)
        help.addAction(Checkupdate)
        Checkupdate.triggered.connect(lambda:update.check(self))
        licence=qt1.QAction(_("license"),self)
        help.addAction(licence)
        licence.triggered.connect(lambda: Licence(self))
        donate=qt1.QAction(_("donate"),self)
        help.addAction(donate)
        donate.triggered.connect(lambda:guiTools.OpenLink(self,"https://www.paypal.me/AMohammed231"))
        about=qt1.QAction(_("about"),self)
        help.addAction(about)
        about.triggered.connect(lambda:qt.QMessageBox.information(self,_("about"),_("{} version: {} description: {} developer: {}").format(app.name,str(app.version),app.description,app.creater)))
        self.setMenuBar(mb)
        if settings_handler.get("update","autoCheck")=="True":
            update.check(self,message=False)
    def closeEvent(self, event):
        if settings_handler.get("g","exitDialog")=="True":
            m=guiTools.ExitApp(self)
            m.exec()
            if m:
                event.ignore()
        else:
            self.close()
    def on_select_file(self):
        file=qt.QFileDialog(self)
        if file.exec()==file.DialogCode.Accepted:
            self.path.setText(file.selectedFiles()[0])
    def on_select_output_folder(self):
        folder=qt.QFileDialog()
        folder.setFileMode(folder.FileMode.Directory)
        if folder.exec()==folder.DialogCode.Accepted:
            self.outputDir.setText(folder.selectedFiles()[0])
    def on_select_image_file(self):
        file=qt.QFileDialog(self)
        if file.exec()==file.DialogCode.Accepted:
            self.imagePath.setText(file.selectedFiles()[0])

App=qt.QApplication([])
w=main()
w.show()
App.setStyle('fusion')
App.exec()