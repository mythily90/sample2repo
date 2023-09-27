import socket
from _thread import *

HOST = ''
PORT = 8053
dnstable = dict()


def clientconn(conn):
    while True:
        data = conn.recv(1024)
        if not data: 
            break
        datalist = data.decode('utf8').strip().split(' ')
        finaladdr = ""
        if datalist[0] == "get":
            if len(datalist) != 2:
                finaladdr = "Error only one domain can be asked for resolving "
            else:
                if datalist[1] in dnstable:
                    finaladdr = dnstable[datalist[1]]
                else:
                    finaladdr = "Server cant find domain {}".format(datalist[1])
        elif datalist[0] == "put":
            if len(datalist) != 3:
                finaladdr = "Error: put damian_name addr is the format"
            else:
                dnstable[datalist[1]] = datalist[2]
                finaladdr = "Domain details added"
        else:
            finaladdr= "Invalid input. Only get or put supported"
        conn.sendall(bytes(finaladdr+'\n','utf8'))
    conn.close()


def main():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST,PORT))
    s.listen()
    while True:
        con, addr = s.accept()
        print ('Connected By ', addr)
        start_new_thread(clientconn, (con,))
    s.close()

if __name__=='__main__':
    main()
