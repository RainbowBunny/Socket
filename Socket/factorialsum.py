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
  smt = (tn.recv())
  print(smt)
  if smt[0] == 1:
    print(smt)
  else:
    print(smt + tn.recv())
    break