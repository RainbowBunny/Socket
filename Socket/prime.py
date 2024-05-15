from pwn import *
from Crypto.Util.number import isPrime

tn = connect("112.137.129.129", 27003)
tn.send(p32(0) + p32(8) + b"22021105")

while True:
  smt = (tn.recv(12))
  print(smt)
  if smt[0] == 1:
    n = int.from_bytes(smt[8 : 12], "little") + 1
    print(n)
    while not isPrime(n):
      n += 1
    print(n)
    tn.send(p32(2) + p32(4) + p32(n))
  else:
    print(smt + tn.recv())