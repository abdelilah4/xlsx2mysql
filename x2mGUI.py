# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\2py\xlsx reader\x2mGUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
import os
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
import reader,sys
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

def unilong(x): 
    typ = type(x) 
    if typ.__name__ == 'long': 
        x= str(x) 
    elif typ.__name__ == 'unicode': 
        x = x.encode('utf8') 
    return x 
def rms(x): 
    x = unilong(x) 
    x = x.replace('-','') 
    x = x.replace('\'','') 
    x = x.replace('/','') 
    x = x.replace('%','') 
    x = x.replace('!','') 
    x = x.replace('?','') 
    x = x.replace('*','') 
    x = x.replace('+','') 
    x = x.replace('.','') 
    x = x.replace('"','') 
    x = x.replace('=','') 
    x = x.replace(' ','') 
    x = x.replace('*','') 
    return x

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(560, 300)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout.addWidget(self.checkBox, 7, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(225, 0))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout.addWidget(self.label_11)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 10, 0, 1, 2)

        self.label_20 = QtGui.QLabel(self.centralwidget)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(self.centralwidget)
        self.label_21.setObjectName(_fromUtf8("label_21"))

        
        self.label_22 = QtGui.QLabel(self.centralwidget)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.label_23 = QtGui.QLabel(self.centralwidget)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        
        self.gridLayout.addWidget(self.label_20, 11, 0, 1, 2)
        self.gridLayout.addWidget(self.label_21, 11, 1, 1, 2)
        self.gridLayout.addWidget(self.label_22, 12, 0, 1, 2)
        self.gridLayout.addWidget(self.label_23, 12, 1, 1, 2)

        
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        #1
        self.gridLayout.addWidget(self.label_10, 6, 0, 1, 1)
        
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox, 5, 1, 1, 1)
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout.addWidget(self.label_13, 8, 1, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(225, 24))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_3.addWidget(self.label_14)
        self.gridLayout.addLayout(self.horizontalLayout_3, 6, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        MainWindow.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        MainWindow.setTabOrder(self.lineEdit_4, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.comboBox)
        MainWindow.setTabOrder(self.comboBox, self.pushButton_4)
        MainWindow.setTabOrder(self.pushButton_4, self.checkBox)
        MainWindow.setTabOrder(self.checkBox, self.pushButton_2)
        self.saveFile2 = ''
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("pressed()")), self.open)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("pressed()")), self.save)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("pressed()")), self.testing)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showup)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "x2mGUI", None))
        self.label_9.setText(_translate("MainWindow", "statut :", None))
        self.label_20.setText(_translate("MainWindow", "Contact us :", None))
        self.label_21.setText(_translate("MainWindow", "on <a href='mailto:abdelilahfadil2@gmail.com'>Email</a> and <a href='https://github.com/abdo0147/x2m/'>Github</a>.", None))
        self.label_22.setText(_translate("MainWindow", "Created By : ", None))
        self.label_23.setText(_translate("MainWindow", "Abd Elilah. ", None))
        self.checkBox.setText(_translate("MainWindow", "do you want a dispaly file ?", None))
        self.pushButton_3.setText(_translate("MainWindow", "import", None))
        self.label_11.setText(_translate("MainWindow", "", None))
        self.pushButton_2.setText(_translate("MainWindow", "start building", None))
        self.label.setText(_translate("MainWindow", "host :", None))
        self.label_3.setText(_translate("MainWindow", "password :", None))
        self.label_2.setText(_translate("MainWindow", "username :", None))
        self.label_4.setText(_translate("MainWindow", "db name :", None))
        self.label_5.setText(_translate("MainWindow", "xlsx file :", None))
        self.label_6.setText(_translate("MainWindow", "tables in xlsx:", None))
        self.label_7.setText(_translate("MainWindow", "option :", None))
        self.label_10.setText(_translate("MainWindow", "save directory :", None))
        self.label_13.setText(_translate("MainWindow", "", None))
        self.pushButton_4.setText(_translate("MainWindow", "save", None))
        self.label_14.setText(_translate("MainWindow", "", None))
        
    def open(self):
       self.label_13.setText('wait ...')
       self.fileName = QtGui.QFileDialog.getOpenFileName(None, 'select File', '.',"Exel files (*.xlsx)")
       self.label_11.setText(self.fileName)
       self.label_13.setText('wait ...')
       self.comboBox.clear()
       if self.fileName=='':
           pass
       else:
           tables = reader.infoxlsx(str(self.fileName))
           self.comboBox.clear()
           self.label_13.setText("loading tables ...")
           for j in tables:
               stb = "seting up "+str(j)
               self.label_13.setText(stb)
               self.comboBox.addItem(_fromUtf8(j))
               stb = str(j)+" loaded."
               self.label_13.setText(stb)
           self.label_13.setText("tables is ready.")

           
    def save(self):
        self.saveFile = QtGui.QFileDialog.getSaveFileName(None,'save into :','.','*.php')
        self.label_14.setText(self.saveFile)
        a = os.path.basename(str(self.saveFile))
        b = a.replace('.php','-diplay-file.php')
        d = os.path.dirname(str(self.saveFile))
        self.saveFile2 = d+"/"+b

        
    def showup(self):
        self.check = self.checkBox.isChecked()
        if self.check == True:
            if self.saveFile2 == '' or self.saveFile2 == '/':
                pass
            else:
                self.label_13.setText("it will be named in : "+self.saveFile2)
        else:
            self.label_13.setText("")
            


    def start(self,host,username,password,database,check,fil,table,output,dfile):
        #script
        print '[*] setup settings to buil the php script'
        self.label_13.setText('[*] setup settings to buil the php script')
        #print '        Tables exists on the file:', 
        #tables = reader.infoxlsx(fil) 
        #print ' , '.join(tables) 
        tab = rms(table) 
        lista = reader.Readxlsx(fil,table) 
        if len(lista)==0: 
            print 'Table',table,'is empty.'
            self.label_13.setText('Table '+str(table)+' is empty.')
            sys.exit() 
        else: 
            pass 
        f = open(output,'w+') 
        f.writelines( '<?php\n\n$host = "'+host+'";\n$username = "'+username+'";\n$password = "'+password+'";\n$database = "'+database+'";\n\n// Create connection\n\n$conn = new mysqli($host, $username, $password,$database);\n\n// Check connection\n\nif ($conn->connect_error) {\n\n    die("Connection failed: " . $conn->connect_error);\n\n}') 
        f.writelines('\nset_time_limit(200);\n') 
        f.writelines('\n$sqltabel = "CREATE TABLE '+tab+'(\n      id MEDIUMINT NOT NULL AUTO_INCREMENT,\n') 
        j=0 
        for i in lista[0]: 
            j=j+1 
            if i==None: 
                sj = 'None'+str(j) 
                sj=rms(sj) 
                f.writelines( '      '+sj+' TEXT NOT NULL,\n') 
            else: 
                i=rms(i) 
                f.writelines( '      '+str(i)+' TEXT NOT NULL,\n') 
 
        f.writelines( '     PRIMARY KEY (id));";\n') 
        f.writelines( 'if ($conn->query($sqltabel) === TRUE) { echo "Table '+tab+' created.\n";} else {echo "Table not created: " . $conn->error."</br>";}') 
        headers = list() 
        j=0 
        for i in lista[0]: 
            if i == None: 
                j=j+1 
                h='None'+str(j) 
                headers.append(h) 
                h='' 
            else: 
                i=rms(i) 
                headers.append(i) 
 
        com = '$sql = \'insert into '+tab+' ('+','.join(headers)+') values(' 
        j = 0 
        f.writelines( '\n') 
        for i in lista: 
            if j==0: 
                j=j+1 
                pass 
            else: 
                j = j+1 
                f.writelines(com) 
                m = 0 
                for k in i: 
                    if m==len(i)-1: 
                        if k ==None: 
                            f.writelines('"None"') 
                        else: 
                            k=unilong(k) 
                            k = (str(k)).replace("'","\\'") 
                            k = (str(k)).replace('"','\\"') 
                            f.writelines('"'+str(k)+'"') 
                    else: 
                        m = m+1 
                        if k ==None: 
                            f.writelines('"None",') 
                        else: 
                            k = unilong(k) 
                            k = (str(k)).replace("'","\\'") 
                            k = (str(k)).replace('"','\\"') 
                            f.writelines('"'+str(k)+'",') 
                f.writelines(')\';\n') 
                f.writelines( 'if ($conn->query($sql) === TRUE) { echo "data inserted.</br>"; } else {echo "Data not inserted: " . $conn->error."</br>";}\n') 
        f.writelines('$conn->close();') 
        f.writelines('\n?>') 
        f.close()
        print '[*] php file: '+output+' builded'
        self.label_13.setText('[*] php file: '+output+' builded')
        if check == 'True': 
            nf = open(dfile,'w+') 
            nf.writelines( '<?php\n\n$host = "'+host+'";\n$username = "'+username+'";\n$password = "'+password+'";\n$database = "'+database+'";\n\n// Create connection\n\n$conn = new mysqli($host, $username, $password,$database);\n\n// Check connection\n\nif ($conn->connect_error) {\n\n    die("Connection failed: " . $conn->connect_error);\n\n}') 
            nf.writelines('\nset_time_limit(200);\n') 
            nf.writelines('$sql = \'select id,'+','.join(headers)+' from '+tab+'\';\n') 
            nf.writelines('echo "<style>\ntr:hover {\nbackground: #DBECF9;\n}\ntr:active {\nbackground: #9DCCEE;\n}\ntr {\nbackground: ;\n}\n</style>";') 
            display = 'echo "<table border=\'1\'  width=\'100%\' cellspacing=\'0\' cellpadding=\'0\' bordercolorlight=\'#993333\' bordercolordark=\'#FF0000\'>\n<tr>' 
            nf.writelines(display) 
            for i in headers: 
                display = '<td>'+str(i)+'</td>' 
                nf.writelines(display) 
            nf.writelines('</tr>";\n') 
            nf.writelines('$result = $conn->query($sql);\n') 
            nf.writelines( 'if ($result->num_rows > 0) {\n// output data of each row\nwhile($row = $result->fetch_assoc()) {\n') 
            nf.writelines('echo "<tr>') 
            for i in headers: 
                display = '<td>".$row["'+str(i)+'"]."</td>' 
                nf.writelines(display) 
                nf.writelines('\n   ') 
            nf.writelines('</tr>";\n') 
            nf.writelines('    }\n} else {\n    echo "0 results";}\n') 
            nf.writelines('echo "</table>";\n') 
            nf.writelines('$conn->close();\n?>') 
            nf.close()
            print '[*] '+dfile+' builded.'
            self.label_13.setText('[*] '+dfile+' builded.')
        print '[*] script by Abd Elilah.'
    def testing(self):
       self.host = self.lineEdit.text()
       self.username = self.lineEdit_2.text()
       self.password = self.lineEdit_3.text()
       self.db =  self.lineEdit_4.text()
       self.check = self.checkBox.isChecked()
       self.table = self.comboBox.currentText()
       msg = QMessageBox()
       msg.setIcon(QMessageBox.Information)
       msg.setText("Final step")
       msg.setInformativeText("Are you sure you want to continue?")
       msg.setWindowTitle("Final step")
       details = "The details are as follows:\nhost :"+str(self.host)+'\nusername :'+str(self.username)+'\npassword :'+str(self.password)+'\ndatabase name :'+str(self.db)+'\nfile name :'+str(self.fileName)+'\nsave file: '+str(self.saveFile)+'\ntable selected :'+str(self.table)+'\ncreate display file :'+str(self.check)+'\ndisplay file name: '+str(self.saveFile2)
       msg.setDetailedText(details)
       msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
       msg.buttonClicked.connect(self.msgbtn)
	
       self.retval = msg.exec_()
       
	
    def msgbtn(self,i):
       print "Button pressed is:",i.text()
       if str(i.text())=='OK':
           print "collect all data :(",
           print self.host,',',self.username,',',self.password,',',self.db,',',self.check,',',self.fileName,',',self.saveFile,',',self.table,',',self.saveFile2,')'
           self.start(str(self.host),str(self.username),str(self.password),str(self.db),str(self.check),str(self.fileName),str(self.table),str(self.saveFile),str(self.saveFile2))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

