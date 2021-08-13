import _thread
import socket
import threading
"""AF_INET is the address domain of the 
socket. This is used when we have an Internet Domain with 
any two hosts The 2nd context of the code is the type of socket. """
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# piece of code to allow IP address & Port
host="127.0.0.1"
port=5000
s.bind((host,port))
s.listen(5)
clients=[]
#code to allow users to send messages
def connectNewClient(c):
     while True:
        global clients
        msg = c.recv(2048)
        msg ='Online ('+str(clients.index(c)+1)+'):  '+msg.decode('ascii')
        sendToAll(msg,c)
def sendToAll(msg,con):
    for client in clients:
        client.send(msg.encode('ascii')) 
        
while True:
    c,ad=s.accept()
    # Display message when user connects
    print('*Server Connected ')
    clients.append(c)
    c.send(('Online ('+str(clients.index(c)+1)+')').encode('ascii'))
    _thread.start_new_thread(connectNewClient,(c,))
