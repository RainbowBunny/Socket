from pwn import *
from Crypto.Util.number import GCD

tn = connect("112.137.129.129", 27002)
tn.send(p32(0) + p32(8) + b"22021105")

print(tn.recv(8))
while True:
  smt = (tn.recv(20))
  print(smt)
  if smt[0] == 1:
    N = int.from_bytes(smt[8 : 12], "little")
    M = int.from_bytes(smt[12 : 16], "little")
    x = int.from_bytes(smt[16 : 20], "little")
    ans = 0
    cur = 1

    for i in range(N + 1):
      A = int.from_bytes(tn.recv(4), "little")
      ans = (ans + A * cur) % M
      cur = (cur * x) % M
    
    tn.send(p32(2) + p32(4) + p32(ans))
  else:
    print(smt + tn.recv())
    break