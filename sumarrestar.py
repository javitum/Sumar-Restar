# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot ,  QSettings
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore ,  QtWidgets , QtMultimedia
import sys
from random import randint
from Ui_sumarrestar import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.trans=QtCore.QTranslator(self)
        idiomas=['Español', 'English']
        self.comboBoxIdioma.addItems(idiomas)
        
        self.settings = QSettings('javitum', 'SumarRestar')
        self.cargar_configuracion()
        
    
    @pyqtSlot()
    def on_pushButtonSalir_clicked(self):
        MainWindow.guardar_configuracion(self)
        sys.exit()
    
    @pyqtSlot()
    def on_pushButtonReiniciar_clicked(self):
        self.textEditllevadas1.setText("")
        self.textEditllevadas2.setText("")
        self.textEditllevadas3.setText("")
        self.textEditllevadas4.setText("")
        self.lineEditdecenasdemillares.setText("")
        self.lineEditmillares.setText("")
        self.lineEditcentenas.setText("")
        self.lineEditdecenas.setText("")
        self.lineEditunidades.setText("")
        self.labelresultado_2.setText("")
        self.labelresultado.setText("")
        self.labelejercicios.setText("0")
        self.labeloperacion1.setText("")
        self.labeloperacion2.setText("")
        self.labelbien.setText("0")
        self.labelmal.setText("0")
        self.labelnota.setText("")
        self.labelsigno.setText("")
        self.pushButtonGenerar.setEnabled(True)
        self.pushButtonComprobar.setEnabled(False)
        self.corazon.setGeometry(1260,520,1,1)
        MainWindow.guardar_configuracion(self)  
        
    @pyqtSlot(str)
    def on_comboBoxIdioma_currentIndexChanged(self, p0):
        idiomas={'Español':'', 'English':'en'}
        idioma_seleccionado=idiomas[p0]
        if idioma_seleccionado:
            self.trans.load(str(idioma_seleccionado))
            QtWidgets.QApplication.instance().installTranslator(self.trans)
        else:
            QtWidgets.QApplication.instance().removeTranslator(self.trans)
        self.retranslateUi(MainWindow)



    
    @pyqtSlot()
    def on_pushButtonComprobar_clicked(self):
        if self.lineEditdecenasdemillares.text()=="":
            decenasdemillares=0
        else:
            decenasdemillares=int(self.lineEditdecenasdemillares.text())*10000
        if self.lineEditmillares.text()=="":
            millares=0
        else:
            millares=int(self.lineEditmillares.text())*1000            
        if self.lineEditcentenas.text()=="":
            centenas=0
        else:
            centenas=int(self.lineEditcentenas.text())*100
        if self.lineEditdecenas.text()=="":
            decenas=0
        else:
            decenas=int(self.lineEditdecenas.text())*10
        if self.lineEditunidades.text()=="":
            unidades=0
        else:
            unidades=int(self.lineEditunidades.text())
        miresultado=decenasdemillares+millares+centenas+decenas+unidades
        signo=self.labelsigno.text()
        num1=int(self.labeloperacion1.text())
        num2=int(self.labeloperacion2.text())
        if signo=="+":
            resultado=num1+num2
        else:
            resultado=num1-num2
        
        self.labelresultado.setText(str(resultado)) 
        if miresultado==resultado:
            self.labelresultado_2.setText(self.tr("Bien")) 
            bien=int(self.labelbien.text())+1
            self.labelbien.setText(str(bien))

        else:
            self.labelresultado_2.setText(self.tr("Mal") )
            mal=int(self.labelmal.text())+1
            self.labelmal.setText(str(mal))
        
        ejercicios=int(self.labelejercicios.text())+1
        self.labelejercicios.setText(str(ejercicios))
        bien=int(self.labelbien.text())
        nota=(bien/ejercicios)*10
        self.labelnota.setText(str(nota))
        self.pushButtonGenerar.setEnabled(True)
        self.pushButtonComprobar.setEnabled(False)
        self.pushButtonGenerar.setFocus()
        
        ejercicios_min=int(self.lineEditEjercicios_min.text())
        nota_min=int(self.lineEditNota_min.text())
        
        if ejercicios>=ejercicios_min and nota>=nota_min:
            self.corazon.setGeometry(1260,520,220,216)
            self.pushButtonGenerar.setEnabled(False)
            self.pushButtonComprobar.setEnabled(False)
            filename = 'Aplausos.mp3'
            #fullpath = QtCore.QDir.current().absoluteFilePath(filename) 
            media = QtCore.QUrl.fromLocalFile(filename)
            content = QtMultimedia.QMediaContent(media)
            self.player = QtMultimedia.QMediaPlayer()
            self.player.setMedia(content)
            self.player.play()

  
    
    @pyqtSlot()
    def on_pushButtonGenerar_clicked(self):
        tablas=[]
        self.textEditllevadas1.setText("")
        self.textEditllevadas2.setText("")
        self.textEditllevadas3.setText("")
        self.textEditllevadas4.setText("")
        self.lineEditdecenasdemillares.setText("")
        self.lineEditmillares.setText("")
        self.lineEditcentenas.setText("")
        self.lineEditdecenas.setText("")
        self.lineEditunidades.setText("")
        self.labelresultado_2.setText("")
        self.labelresultado.setText("")

        
        if self.checkBox_sumar.isChecked()==True:
            tablas.append(1)
        if self.checkBox_restar.isChecked()==True:
            tablas.append(2)
        n_tablas=len(tablas)
        tablaoperacion=tablas[randint(0, n_tablas-1)]
        if tablaoperacion==1:
            self.labelsigno.setText("+") 
            self.textEditllevadas4.setGeometry(330, 350, 40, 40)
            self.textEditllevadas3.setGeometry(400, 350, 40, 40)
            self.textEditllevadas2.setGeometry(480, 350, 40, 40)
            self.textEditllevadas1.setGeometry(550, 350, 40, 40)
        if tablaoperacion==2:
            self.labelsigno.setText("-")
            self.textEditllevadas4.setGeometry(330, 646, 40, 40)
            self.textEditllevadas3.setGeometry(400, 646, 40, 40)
            self.textEditllevadas2.setGeometry(480, 646, 40, 40)
            self.textEditllevadas1.setGeometry(550, 646, 40, 40)
        
        cifras_multiplicando=[]
        if self.checkBox_11.isChecked()==True:
            cifras_multiplicando.append(1)
        if self.checkBox_12.isChecked()==True:
            cifras_multiplicando.append(2)
        if self.checkBox_13.isChecked()==True:
            cifras_multiplicando.append(3)
        if self.checkBox_14.isChecked()==True:
            cifras_multiplicando.append(4)
        if self.checkBox_15.isChecked()==True:
            cifras_multiplicando.append(5)      
        n_cifras=len(cifras_multiplicando)
        cifrasaleatoria1=cifras_multiplicando[randint(0, n_cifras-1)]
        cifrasaleatoria2=cifras_multiplicando[randint(0, n_cifras-1)]  
        cifra1=randint(1, ((10**cifrasaleatoria1)-1))
        cifra2=randint(1, ((10**cifrasaleatoria2)-1))
        if tablaoperacion==2 and cifra1<cifra2:
            cifra1, cifra2=cifra2, cifra1

        self.labeloperacion1.setText(str(cifra1))
        self.labeloperacion2.setText(str(cifra2))
        self.pushButtonGenerar.setEnabled(False)
        self.pushButtonComprobar.setEnabled(True)
        self.lineEditunidades.setFocus()
    
    def guardar_configuracion(self):
        self.settings.setValue('idioma', self.comboBoxIdioma.currentText())
        self.settings.setValue('ejer_min', self.lineEditEjercicios_min.text())
        self.settings.setValue('nota_min', self.lineEditNota_min.text())
        self.settings.setValue('sumar', self.checkBox_sumar.isChecked())
        self.settings.setValue('restar', self.checkBox_restar.isChecked() )
        self.settings.setValue('1', self.checkBox_11.isChecked())
        self.settings.setValue('2', self.checkBox_12.isChecked())
        self.settings.setValue('3', self.checkBox_13.isChecked())
        self.settings.setValue('4', self.checkBox_14.isChecked())
        self.settings.setValue('5', self.checkBox_15.isChecked())
        
    def cargar_configuracion(self):
        self.comboBoxIdioma.setCurrentText(self.settings.value('idioma'))
        self.lineEditEjercicios_min.setText(self.settings.value('ejer_min'))
        self.lineEditNota_min.setText(self.settings.value('nota_min'))
        self.checkBox_sumar.setChecked(eval(self.settings.value('sumar').capitalize()))
        self.checkBox_restar.setChecked(eval(self.settings.value('restar').capitalize()))
        self.checkBox_11.setChecked(eval(self.settings.value('1').capitalize()))
        self.checkBox_12.setChecked(eval(self.settings.value('2').capitalize()))
        self.checkBox_13.setChecked(eval(self.settings.value('3').capitalize()))
        self.checkBox_14.setChecked(eval(self.settings.value('4').capitalize()))
        self.checkBox_15.setChecked(eval(self.settings.value('5').capitalize()))

