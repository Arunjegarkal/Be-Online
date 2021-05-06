# -*- coding: utf-8 -*-

"""
Created on Mon May  3 10:13:17 2021

@author: Arun.Jegarkal
"""
import tkinter as tk
#import event         
import threading
from pynput.keyboard import Key,Controller
import time
from tkinter import messagebox



#initiate the keyboard event
def press_event():  
    print ("press event")
    keyboard = Controller()
    global IsStop
    #press space bar every 30 sec
    while IsStop==False:
        print ("IsStop ",IsStop," id ",id)
        #print (i)
        print ("pressed ",keyboard.press(Key.space))
        print ("released",keyboard.release(Key.space))
        time.sleep(30)
        
        #if IsStop:
        #    print("stopped thread")
        #    break

#When closed the application terminate all active threads by activating the IsStop         
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        global IsStop
        IsStop=True
        root.destroy()


def start_event():
    global root
    global threads
    global IsStop
    global eventStatus
    global statusLabel
    threads=[]
    eventStatus="Being Online event has been initiated"
    IsStop = False
    statusLabel.config(text=eventStatus)
    canvas.create_window(150,200, window=statusLabel)
    #event.start_event()
    d = threading.Thread(name='start',target=press_event)
    threads.append(d)
    d.start()
    
#stop all the active threads    
def stop_event():
    global root
    global threads
    global IsStop
    print ("stop_event")
    IsStop= True
    global eventStatus
    global statusLabel
    print ("current running  threads",len(threads)) 
    eventStatus="Being Online event is stopped"
    #canvas.itemconfig(statusLabel,text=eventStatus)
    statusLabel.config(text = eventStatus)
    
        
def main():
    global root
    str_btn = tk.Button(root,text="Start Event", command=start_event,bg='brown', fg='white')    
    canvas.create_window(100,150, window=str_btn)    
    stp_btn = tk.Button(root,text="Stop Event", command=stop_event,bg='brown', fg='white')    
    canvas.create_window(200,150, window=stp_btn)   
    author = tk.Label(root,text="Developer : Arun Jegarkal \n contact : arunjegarkal@gmail.com")
    canvas.create_window(200,250,window=author)
    root.mainloop()

root = tk.Tk()
root.title("Be Online")
canvas = tk.Canvas(root,width = 300, height = 300)
canvas.pack()

statusLabel = tk.Label(root,text = "", fg='green', font = ('helvetica', 12, 'bold'))
root.protocol("WM_DELETE_WINDOW", on_closing)    

if __name__== "__main__":
    main()