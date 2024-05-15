from pwn import *
from Crypto.Util.number import isPrime

tn = connect("112.137.129.129", 27016)

tn.send(p32(0) + p32(8) + b"22021105")

# prime 2 la tim so nguyen to lon nhat nho hon n

while True:
  smt = (tn.recv(16))
  print(smt)
  if smt[0] == 1:
    m = int.from_bytes(smt[8 : 12], "little")
    leng = int.from_bytes(smt[4 : 8], "little") // 4 - 2
    checksum = int.from_bytes(smt[12 : 16], "little")
    A = []
    for i in range(leng):
      A.append(int.from_bytes(tn.recv(4), "little"))
    sm = sum(A)
    cur, ans = 0, -1
    com = 1
    for i in range(leng):
      if 2 * cur == sm - A[i]:
        ans = i
      cur += A[i]
      com = com * A[i] % m
      print(cur, sm)
    print(A, ans + 1)
    if checksum != com:
      print("Nooooo")
      tn.send(p32(2) + p32(4) + p32(0))
    else:
      print(ans, cur)
      tn.send(p32(2) + p32(8) + p32(1) + p32(ans))
  else:
    print(smt + tn.recv())