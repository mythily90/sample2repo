from concurrent.futures import thread
from threading import Thread
import socket

HOST = ''
PORT = 8054
dnstable = dict()

def getRecord(msglist):
    if len(msglist) != 2:
        return "get input format is get <<addr>>"
    if msglist[1] in dnstable:
        return dnstable[msglist[1]]
    else:
        return "Server cant found {}".format(msglist[1])

def putRecord(msglist):
    if len(msglist) !=3:
        return "put input format should be put <<domain>> <<addr>>"
    dnstable[msglist[1]] = msglist[2]
    return "Successfully added record"


def connHandler(clientconn):
    while True:
        msg = clientconn.recv(1024)
        if not msg: break
        msglist = msg.decode('utf-8').strip().split(' ')
        if msglist[0] == "get": 
            dataToReturn = getRecord(msglist)
        elif msglist[0] == "put":
            dataToReturn = putRecord(msglist)
        else:
            dataToReturn = "Invalid Input"
        clientconn.sendall(bytes(dataToReturn+"\n",'utf-8'))
    clientconn.close()
        



def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST,PORT))
    s.listen()

    while True:
        conn, addr = s.accept()
        print("Connected by ",addr)
        connthread = Thread(target=connHandler, args = (conn,))
        connthread.start()
        print("Exiting connection ", addr)


if __name__ == "__main__":
    main()