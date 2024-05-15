from pwn import *
from Crypto.Util.number import GCD

tn = connect("112.137.129.129", 27012)
print(tn.recv())
tn.send(p32(0, endian = "big") + p32(8, endian = "big") + b"22021105")

while True:
  smt = (tn.recv())

  print(smt)
  if smt[0] == 1:
    n = int.from_bytes(smt[8 : 16], "big")
    print(n)
    tn.send(p32(2) + p32(8) + p64(n))
  else:
    print(smt)
    break