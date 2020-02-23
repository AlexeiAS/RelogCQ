from functools import partial
import threading
import queue
import time


def newRead(label,index,g):
    minute = g.qtime.filas[index][0] 
    second = g.qtime.filas[index][1]
    label["text"] = str(minute) + " : " + str(second)



def Rwrite(minute,second,label,buttom,index,g):
    while(True):
        tempo = time.localtime()
        for m in range(0,minute):
                for s in range(0,second):
                    if(g.qreset.isZero(index)==1):
                        label["text"] = "0 : 0"
                        g.qreset.changeValue(index)
                        g.qstart.changeValue(index)
                        if(g.qpause.isZero(index) == 1):
                            g.qpause.changeValue(index)
                        return threading.main_thread()
                    if(g.qpause.isZero(index) == 1):
                        while(g.qpause.isZero(index) == 1):
                            if(g.qreset.isZero(index)==1):
                                g.qpause.changeValue(index)
                                label["text"]="0 : 0"
                                buttom["text"]="p"
                                g.qreset.changeValue(index)
                                g.qstart.changeValue(index)
                                return threading.main_thread()
                            time.sleep(0.5)
                    g.qtime.time(index,m,s)
                    ctempo = time.localtime()

                    #teste:
                    newRead(label,index,g)
                    if ((ctempo[4] == tempo[4]+minute and ctempo[5] == tempo[5]) or (ctempo[3]>tempo[3])):
                        break
                    time.sleep(1)
def Rread(label,index,g):
##    while(True):
##        time.sleep(1)
##        try :
##            
##            if (g.qreset.isZero(index)==1):
##                return threading.main_thread()
##            minute = g.qtime.filas[index][0] 
##            second = g.qtime.filas[index][1]
##            label["text"] = str(minute) + " : " + str(second)
##        except:
##            pass
    pass

    
def bt_start(minute,second,label,buttom,index,g):
    if(g.qstart.isZero(index) == 0):
        g.qstart.changeValue(index)
        if(g.qreset.isZero(index) == 1):
            g.qreset.changeValue(index)
        st = threading.Thread(target = Rwrite,args=(minute,second,label,buttom,index,g,))
        res = threading.Thread(target = Rread,args=(label,index,g,))
        res.start()
        st.start()
        

def bt_reset(index,g):
    if(g.qreset.isZero(index)==0):
        g.qreset.changeValue(index)
        


def bt_pause(buttom,index,g):
    if(g.qpause.isZero(index)==0):
        buttom["text"] = "x"
        g.qpause.changeValue(index)
    else :
        g.qpause.changeValue(index)
        buttom["text"] = "p"
