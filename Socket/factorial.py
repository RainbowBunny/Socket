from pwn import *
from Crypto.Util.number import GCD

tn = connect("112.137.129.129", 27010)
tn.send(p32(0) + p32(8) + b"22021105")

def nhuan(n):
  if n % 400 == 0:
    return True
  if n % 100 == 0:
    return False
  return n % 4 == 0

# an duoc flag bai 27010

while True:
  smt = (tn.recv(16))
  print(smt)
  if smt[0] == 1:
    n = int.from_bytes(smt[8 : 16], "little")
    if (nhuan(n)):
      tn.send(p32(2) + p32(4) + b"Nam nhuan")
    else:
      tn.send(p32(2) + p32(4) + b"Nam khong nhuan")
  else:
    print(smt + tn.recv())
    break