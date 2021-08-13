#Gui Programming Part
import tkinter
import socket
import _thread
import sys

# Code to create a new client socket  and connect to the server

i = 3
client = 0
start = True
def sendMessage ():
    msg = txt.get()
    client.send(msg.encode('ascii'))

def recievingMessage (c): 
    global i
    while True :
        msg=c.recv(2048).decode('ascii')
        if not msg :
            sys.exit(0)
        global start
        if (start) :
            start = False
            #tkinter codes starts
            window.title(msg)
            continue
        msglbl = tkinter.Label(window,text=msg)
        msglbl['font']=("Courier",10)
        msglbl['bg']='black'
        msglbl['fg']='#0aff43'
        msglbl['width']=50
        msglbl.grid(columnspan=2,column=0,row=i,padx=5)
        i += 1
#Socket Creation
def socketCreation ():    
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#Local Host    
# import all functions /
#  everthing from chat.py file
    host = '127.0.0.1'
    port = 5000
    c.connect((host,port))
    global client
    client = c
    send['command'] = sendMessage
    _thread.start_new_thread(recievingMessage, (c,) )


#Creating a window
window = tkinter.Tk()
window.title('Chatbox')
window['bg']='#242424'

window['padx']=10
window['pady']=10
#Adding Elements
#Entry
txt = tkinter.Entry(window)
txt['width']=50
txt['relief']=tkinter.GROOVE
txt['bg']='#f5f6f7'
txt['fg']='red'
txt['font']=("Courier",12)
txt.grid(column=0,row=1,padx=5,pady=15)
#Button
send = tkinter.Button(window,text="Send")
send['relief']=tkinter.GROOVE
send['bg']='red'
send['fg']='white'
send['activebackground']='#404040'
send['padx']=3
send['font']=("Courier",10)
send.grid(column=1,row=1,padx=5,pady=15)


_thread.start_new_thread(socketCreation, () )


window.mainloop()
