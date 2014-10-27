#Boa:Frame:Frame1

import wx
import wx.lib.filebrowsebutton
import random
import math

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BTN_EVALUAR, wxID_FRAME1FILEBROWSEBUTTON1, 
 wxID_FRAME1FILEBROWSEBUTTON2, wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, 
 wxID_FRAME1STATICTEXT4, wxID_FRAME1STATICTEXT5, wxID_FRAME1STATICTEXT6, 
 wxID_FRAME1TXT_ALFA, wxID_FRAME1TXT_NO, wxID_FRAME1TXT_RESULTADO, 
 wxID_FRAME1TXT_TOLERANCIA, 
] = [wx.NewId() for _init_ctrls in range(13)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(627, 275), size=wx.Size(445, 653),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame1')
        self.SetClientSize(wx.Size(445, 653))

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'PRACTICA 1 - IA1', name='staticText1', parent=self,
              pos=wx.Point(152, 32), size=wx.Size(162, 20), style=0)
        self.staticText1.SetFont(wx.Font(13, wx.SWISS, wx.NORMAL, wx.BOLD, True,
              u'Cantarell'))

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label=u'Alfa:', name='staticText4', parent=self, pos=wx.Point(48,
              184), size=wx.Size(33, 18), style=0)

        self.txt_alfa = wx.TextCtrl(id=wxID_FRAME1TXT_ALFA, name=u'txt_alfa',
              parent=self, pos=wx.Point(128, 184), size=wx.Size(168, 28),
              style=0, value=u'0.01')

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5,
              label=u'Iteraciones', name='staticText5', parent=self,
              pos=wx.Point(48, 232), size=wx.Size(85, 18), style=0)
        self.staticText5.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Cantarell'))

        self.txt_no = wx.TextCtrl(id=wxID_FRAME1TXT_NO, name=u'txt_no',
              parent=self, pos=wx.Point(128, 224), size=wx.Size(168, 28),
              style=0, value=u'10')

        self.btn_evaluar = wx.Button(id=wxID_FRAME1BTN_EVALUAR,
              label=u'Evaluar', name=u'btn_evaluar', parent=self,
              pos=wx.Point(182, 296), size=wx.Size(85, 30), style=0)
        self.btn_evaluar.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_FRAME1BTN_EVALUAR)

        self.staticText6 = wx.StaticText(id=wxID_FRAME1STATICTEXT6,
              label=u'Resultados:', name='staticText6', parent=self,
              pos=wx.Point(48, 336), size=wx.Size(85, 18), style=0)

        self.txt_resultado = wx.TextCtrl(id=wxID_FRAME1TXT_RESULTADO,
              name=u'txt_resultado', parent=self, pos=wx.Point(136, 336),
              size=wx.Size(256, 208), style=wx.TE_MULTILINE, value=u'')

        self.fileBrowseButton2 = wx.lib.filebrowsebutton.FileBrowseButton(buttonText=u'Abrir...',
              dialogTitle=u'Seleccion un archivo', fileMask=u'*.csv',
              id=wxID_FRAME1FILEBROWSEBUTTON2, initialValue='',
              labelText=u'Archivo Y', parent=self, pos=wx.Point(48, 128),
              size=wx.Size(344, 48), startDirectory='.', style=wx.TAB_TRAVERSAL,
              toolTip=u'Presona abrir para navegar hasta el archivo deseado')

        self.fileBrowseButton1 = wx.lib.filebrowsebutton.FileBrowseButton(buttonText=u'Abrir...',
              dialogTitle=u'Seleccione un archivo', fileMask=u'*.csv',
              id=wxID_FRAME1FILEBROWSEBUTTON1, initialValue=u'',
              labelText=u'Archivo X', parent=self, pos=wx.Point(48, 80),
              size=wx.Size(344, 48), startDirectory='.', style=wx.TAB_TRAVERSAL,
              toolTip=u'Presona abrir para navegar hasta el archivo deseado')

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'Tolerancia:', name='staticText2', parent=self,
              pos=wx.Point(48, 272), size=wx.Size(77, 18), style=0)

        self.txt_tolerancia = wx.TextCtrl(id=wxID_FRAME1TXT_TOLERANCIA,
              name=u'txt_tolerancia', parent=self, pos=wx.Point(128, 264),
              size=wx.Size(168, 28), style=0, value=u'0.0001')

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.lista_parametros_x = list()
        self.lista_parametros_y = list()
        self.alfa = 0
        self.tolerancia = 0
        self.m = 0
        self.n = 0
        self.costos = list()
        
    def abrirArchivo(self,path):
        contenido = ""
        print 'Abriendo en: '
        print path
        archivo=open(path,'r')
        return archivo

    def OnButton3Button(self, event):
        self.getParametros()
        event.Skip()
        
    def getRandomNumero(self):
        rand_num = random.uniform(0,5)
        return rand_num

    def getParametros(self):
        self.txt_resultado.AppendText(self.txt_alfa.Value)
        archivox = self.abrirArchivo(self.fileBrowseButton1.GetValue())
        archivoy = self.abrirArchivo(self.fileBrowseButton2.GetValue())
        
        #obtengo los parametros de los controles
        self.alfa = float(self.txt_alfa.GetValue())
        self.iteraciones = int(self.txt_no.GetValue())
        self.tolerancia = float(self.txt_tolerancia.GetValue())
        
        #Obtengo el parametro de cada linea de los archivos
        lineax = archivox.readline()
        lineay = archivoy.readline()
        contador = 0
        while lineax!="" or lineay!="":
            #separo los paramtetros en x
            lista_pars_x = lineax.split(",")
            tam = len(lista_pars_x)
            self.n = tam
            templist = list()
            for i in range(0,tam-1):
                #los agrego a una lista temporal
                templist.append(float(lista_pars_x[i]))
            #agrego la lista completa con los parametros de la linea a la lista global de x
            self.lista_parametros_x.append(templist)
            #agrego los parametros en y a la lista global de y
            self.lista_parametros_y.append(float(lineay))
            lineax = archivox.readline()
            lineay = archivoy.readline()
            contador += 1 
        archivox.close()
        archivoy.close()
        self.m = contador
        print "n = ",self.n
        print "m = ",self.m
        resultado = self.calc_serie()
        self.escArchivo()
            
    def calc_serie(self):
        resultado = 0
        iteracion = 0
        j=0
        while(j<self.n):
        #for j in range(self.n):
            temp = float(self.alfa/self.m)
            for i in range(1,self.m):
                lista_i = self.lista_parametros_x[i]
                x_subj_sup_i = lista_i[j-1]
                resultado = resultado + (self.calc_h(i) - self.get_y(i))*x_subj_sup_i
            resultado = temp * resultado
            resultado = self.getRand() - resultado
            self.costos.append(resultado)
            if(iteracion!=0):
                tol = float(resultado - self.costos[iteracion-1])
                tol = float(math.fabs(tol))
                if(tol<=self.tolerancia):
                    return resultado
            iteracion+=1
            j+=1
            if(j==self.n-1):
                j=0
            if(iteracion==self.iteraciones):
                return 1
                
        
    
    def get_y(self,i):
        return self.lista_parametros_y[i-1]
    
    def calc_h(self,i):
        #calculo el resultado de h sub i
        resultado = 0;
        for k in range(0,i):
            lista_x = self.lista_parametros_x[k]
            tam = len(lista_x)
            for j in range(0,tam):
                thetaRand = self.getRand()
                resultado = resultado + (thetaRand*lista_x[j])
            resultado = resultado + self.getRand()
        return resultado
    
    
    def escArchivo(self):
        f = open('costos.csv','w')
        for i in range(len(self.costos)):
            linea = str(self.costos[i])+"\n"
            f.write(linea)
        f.close()
    
    def getRand(self):
        return random.uniform(0,1)
     
        

