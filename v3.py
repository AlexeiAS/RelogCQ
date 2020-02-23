from tkinter import *
from functools import partial
import threading
import queue
import time
import sys
sys.path.append('C:/Users/willi/Desktop/RegCqV2/funcoes')
import funcoes as f

##class gerenciateste:
##    def startRel(self,rel):
##        if (hasattr(rel,'stArqCount')):
##            rel.stArqCount()
##            return True
##
##        elif(hasattr(rel,'stGravisCount')):
##            rel.stGravisCount()
##            return True
##
##        else:
##            return False
    

class queueAlt:
    def __init__(self):
        self.filas = dict()
        
    def isZero(self,index):
        try:
            if (self.filas[index] == 0):
                return 0
            else:
                return 1
        except:
            return -1
        
    def time(self,index,min,sec):
        self.filas[index] = (min,sec)
        
    def flag(self,index,value):
        self.filas[index] = 0
        
    def changeValue(self,index):
        if (self.filas[index]== 0):
            self.filas[index] = 1
        else:
            self.filas[index] = 0

class relog:
    def __init__ (self,index):
        self.index = index

    def create(self,wdw):
        self.lb = Label(wdw,width=5,text="0 : 0")
        self.bs = Button(wdw,width=1,text="s")
        self.br = Button(wdw,width=1,text="r")
        self.bp = Button(wdw,width=1,text="p")
        
    def funcoes(self,ger):
        self.bs["command"] = partial(f.bt_start,2,60,self.lb,self.bp,self.index,ger)
        self.br["command"] = partial(f.bt_reset,self.index,ger)
        self.bp["command"] = partial(f.bt_pause,self.bp,self.index,ger)

    def place(self,ger):
        self.lb.place(x = 0, y = ger.y)
        self.bs.place (x = 50, y = ger.y)
        self.br.place (x = 70, y = ger.y)
        self.bp.place (x = 90, y = ger.y)
        ger.y +=30
        
    def startRel(self,ger,wdw):
        ger.startQueue()
        self.create(wdw)
        self.funcoes(ger)
        self.place(ger)
        
        
               
    
class gerencia:
    #instancia as filas
    qtime = queueAlt()
    qreset = queueAlt()
    qstart = queueAlt()
    qpause = queueAlt()
    count = 0

    #instancia as posicoes
    y = 10
    def startQueue(self):
        #cria as filas
        self.__class__.count +=1
        aux = self.__class__.count
        self.__class__.qtime.time(aux,0,0)
        self.__class__.qreset.flag(aux,0)
        self.__class__.qstart.flag(aux,0)
        self.__class__.qpause.flag(aux,0)



index = 1
g = gerencia()
window = Tk()
#instancia is relogios
r = relog(index)
s=relog(index+1)

#inicia os relogios
r.startRel(g,window)
s.startRel(g,window)

#estrutura da janela
y = g.y + 25
y = str(y)
geom = "150x" + y + "+100+100"
window.geometry(geom)
window.mainloop()







