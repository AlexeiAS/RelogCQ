from tkinter import *
from functools import partial
import time
import threading




#Funcoes
def Rwrite (self,ger,minute,second):
    while (True):
        tempo = time.localtime()
        for m in range (0,minute):
            for s in range (0,second):
                if (ger.flag == 1):
                    return threading.main_thread()
                if (self.r == 1):
                    self.lb["text"] = "0 : 0"
                    self.r = 0
                    self.s = 0
                    self.p = 0
                    return threading.main_thread()
                if (self.p == 1):
                    while (self.p == 1):
                        if (self.r == 1):
                            self.lb["text"] = "0 : 0"
                            self.r = 0
                            self.s = 0
                            self.p = 0
                            self.bp["text"] = "p"
                            return threading.main_thread()
                        time.sleep(0.5)
                ctempo = time.localtime()
                if ((ctempo[4] == tempo[4]+minute and ctempo[5] == tempo[5]) or (ctempo[3]>tempo[3])):
                    break                
                self.lb["text"] = str(m) + ' : ' + str(s)
                time.sleep(1)
                


def bt_start(self,ger,minute,second):
    if (self.s == 0):
        self.s = 1
        st = threading.Thread(target = Rwrite,args= (self,ger,minute,second,))
        st.start()
    if(self.s == 1):
        pass



def bt_reset(self):
    if (self.s == 1 and  self.r == 0):
        self.r = 1
    else :
        pass
def bt_pause(self):
    if (self.p == 0):
        self.bp["text"] = 'x'
        self.p = 1
    else :
        self.p = 0
        self.bp["text"] = 'p'


#Classes

class relog :
    def __init__ (self):
        self.s = 0
        self.r = 0
        self.p = 0
        
    def create(self,wdw):
        self.lb = Label(wdw,width=5,text = "0 : 0")
        self.bs = Button(wdw, width = 1, text = "s")
        self.br = Button(wdw,width = 1, text = "r")
        self.bp = Button(wdw,width = 1,text = "p")

    def place (self,ger):
        self.lb.place(x=0,y=ger.y)
        self.bs.place(x=50,y=ger.y)
        self.br.place(x=70,y=ger.y)
        self.bp.place(x=90,y=ger.y)

    def funcoes(self,ger):
        self.bs["command"] = partial(bt_start,self,ger,2,60)
        self.br["command"] = partial(bt_reset,self)
        self.bp["command"] = partial(bt_pause,self)

    def start(self,ger,wdw):
        self.create(wdw)
        self.funcoes(ger)
        self.place(ger)
        ger.changeY()
class gerencia :
    y = 10
    flag = 0
    def changeY(self):
        self.__class__.y += 30

def close():
    g.flag = 1
    time.sleep(1)
    window.destroy()

    
#Inicia Janela e Gerenciador
window = Tk()
g = gerencia()
window.protocol('WM_DELETE_WINDOW',close)
#Inicia Relogios
s = relog()
s.start(g,window)
#Estrutura da Janela
y= g.y + 25
y = str(y)
geom = "200x" + y + "+100+100"
window.geometry(geom)
window.mainloop()

