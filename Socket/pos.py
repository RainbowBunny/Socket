from pwn import *
from Crypto.Util.number import GCD

tn = connect("112.137.129.129", 27006)
tn.send(p32(0) + p32(8) + b"22021105")

print(tn.recv(13))
while True:
  smt = (tn.recv(20))
  print(smt)
  if smt[0] == 1:
    x = int.from_bytes(smt[8 : 12], "little")
    N = int.from_bytes(smt[12 : 16], "little")
    M = int.from_bytes(smt[16 : 20], "little")

    print(x, N, M)

    rx, ry = -1, -1
    for i in range(N):
      for j in range(M):
        pos = i * N + M
        v = int.from_bytes(tn.recv(4), "little")
        print(v, end = ' ')
        if v == x and rx == -1:
          rx, ry = i, j
      print()
    if rx == -1:
      rx += 2 ** 32
      ry += 2 ** 32
      tn.send(p32(2) + p32(8) + p32(rx) + p32(ry))
    else:
      print(rx, ry, rx * N + ry)
      tn.send(p32(2) + p32(8) + p32(0) + p32(rx * M + ry))
  else:
    print(smt + tn.recv())
    break