import socket
import struct
import math
 
IP = "112.137.129.129"
PORT = 27005
 
def getAnswer(a, b):
    if b == 0: return a
    return getAnswer(b, a % b)
 
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((IP, PORT))
 
    # hello
    msv = "22021114"
    data = struct.pack("<ii", 0, 8) + msv.encode()
    
    client.send(data)
    data = client.recv(13)

    while True:
        data = client.recv(8)
        print(data + b"owo")
        if not data: 
            print("khong nhan duoc data")
            break
        pkt_type, pkt_len = struct.unpack("<ii", data)
        print(pkt_type, pkt_len)
 
        #calc 
        if pkt_type == 1:
            data = client.recv(8)
            print(data + b"uwu")
            a, b = struct.unpack("<ii", data)
            # answer = getAnswer(a, b)
            answer = math.gcd(a, b)
 
            #result
            data = struct.pack("<iii", 2, 4, answer)
            client.send(data)
        #bye
        elif pkt_type == 3:
            print("Server tu choi ket qua")
            break
        #flag
        elif pkt_type == 4:
            flag = client.recv(pkt_len).decode()
            print(flag)
            break
 
    client.close()
except Exception as e:
    print(e)
    print("Can't connect to server")