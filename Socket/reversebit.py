from pwn import *
from Crypto.Util.number import GCD

tn = connect("112.137.129.129", 27015)
tn.send(b'0 8 22021105')

while True:
  smt = tn.recv()
  print(smt)
  if smt[0] == 49:
    tom = smt.split(b' ')[-1]
    sn = b''
    print(tom)
    for e in reversed(tom):
      sn += chr(e).encode()
    print(int(sn, 2))
    tn.sendline(b'2 8 ' + str(int(sn, 2)).encode() + b' ' + sn)
  else:
    print('Huhu')
    break