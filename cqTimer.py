import pyttsx3
import tkinter as tk
import threading
import time
from functools import partial

engine = pyttsx3.init()                 
engine.setProperty('rate', 200)                    
engine.setProperty('volume',1.0)
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[53].id)

#############################################################################
class flag():
    running = 0
    doalert = 0
    seconds = 0
    stop = 0
    reset = 0

def Alert():
    while True:
        if flag.stop == 1:
            engine.stop()
            return threading.main_thread()
        if flag.doalert == 1:
            
            flag.doalert = 0
            sec = str(flag.seconds)
            engine.say(sec + 'segundos')
            engine.runAndWait()
        time.sleep(0.5)
        
def Counter(label):
    while True:
        if flag.reset == 1:
            flag.reset = 0
        for i in range (2):
            if flag.reset == 1:
                break
            for j in range (60):
                if flag.stop == 1:
                    return threading.main_thread()
                
                if flag.reset == 1:
                    break
                
                label['text'] = str(1 - i) + ' : ' +  str(60 - j)
                if i == 1 and j%15 == 0:
                    flag.seconds = 60 - j
                    flag.doalert = 1
                time.sleep(1)
            
        

def Start(button,label):
    if flag.running ==0:
        flag.stop = 0
        flag.running = 1
        
        counter_thread = threading.Thread(target = Counter,args = (label,))
        alert_thread = threading.Thread(target = Alert)
    
    counter_thread.start()
    alert_thread.start()
    
def Reset(button):
    if flag.reset == 0 and flag.running == 1:
        flag.reset = 1
    
def Stop(button,label):
    if flag.stop == 0 :
        label['text'] = '0:00'
        flag.running = 0
        flag.stop = 1

def close():
    flag.stop = 1
    time.sleep(0.5)
    window.destroy()

    
window = tk.Tk()
window.protocol('WM_DELETE_WINDOW',close)


label = tk.Label(window,width = 5,text = '0:00')
label.pack(pady = 20)

start = tk.Button(window,fg ='white',bg = 'black',width = 5,text = 'Start')
start['command'] = partial(Start,start,label)
start.pack(pady = 10)

reset = tk.Button(window,fg = 'white',bg = 'black',width = 5, text = 'Reset')
reset['command'] = partial(Reset,reset)
reset.pack(pady = 10)

stop = tk.Button(window,fg = 'white',bg = 'black',width = 5, text = 'Stop')
stop['command'] = partial(Stop,stop,label)
stop.pack(pady = 10)



window.geometry('250x250')

window.mainloop()
