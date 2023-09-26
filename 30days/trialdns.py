import socket

HOST = ''
PORT = 8053


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen(1)
    dnstable = dict()
    conn, addr = s.accept()
    with conn:
        print ('Connected By ', addr)
        while True:
            data = conn.recv(1024)
            if not data: break
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
            conn.sendall(bytes(finaladdr+'\n','utf8'))
