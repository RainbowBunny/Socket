import socket
import struct 
import math

IP = "112.137.129.129" 
PORT = 27004

def getAns(a,b,q):
    if ( q == 1):
        return a + b 
    elif ( q == 2):
        return a - b
    elif ( q == 3):
        return a * b 
    elif ( q == 4):
        return pow(a,b)

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect((IP,PORT))
msv = "22021192"
data = struct.pack("<ii" , 0 , 8 ) + msv.encode()
client.send(data)
dem = 1
while True:
    data = client.recv(8)
    print (data )
    print(dem)
    pk_type , pk_len = struct.unpack("<ii" , data)
    print(pk_type , pk_len)
    if (pk_type == 1):
        data = client.recv(12)
        a, b = struct.unpack("<ii" , data[:8])
        q = struct.unpack(">i" , data[8:12])
        x = q[0]
        print ( a , b ,x)
        ans = getAns(a ,b , x)
        print(ans)
        data = struct.pack("<iii" , 2 , 4 , ans)
        client.send(data)
        dem += 1 
    elif (pk_type == 3):
        break
    elif (pk_type == 4):
        print(client.recv(pk_len).decode())
        break
