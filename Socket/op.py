from pwn import *
import time
from Crypto.Util.number import isPrime
import struct

tn = connect("112.137.129.129", 27008)
tn.send(p32(0) + p32(8) + b"22021105")
cao = 0
while True:
  smt = tn.recv(20)
  print(smt)
  cao += 1
  if smt[0] == 1:
    a = int.from_bytes(smt[8 : 12], "little", signed=True)
    b = int.from_bytes(smt[12 : 16], "little", signed=True)
    c = int.from_bytes(smt[16 : 20], "big")
    ans = 0
    if a >= 2 ** 31:
      a -= 2 ** 32
    if b >= 2 ** 31:
      b -= 2 ** 32
    print(a, b, c)
    if c == 1:
      ans = a + b
      if ans < 0:
        ans += 2 ** 32
      tn.send(p32(2) + p32(8) + p32(1, endian = "big") + p32(ans, endian = "big"))
    elif c == 2:
      ans = a - b
      if ans < 0:
        ans += 2 ** 32
      tn.send(p32(2) + p32(8) + p32(1, endian = "big") + p32(ans, endian = "big"))
    elif c == 3:
      ans = a * b
      if ans < 0:
        ans += 2 ** 32
      tn.send(p32(2) + p32(8) + p32(1, endian = "big") + p32(ans, endian = "big"))
    else:
      if (b == 0):
        tn.send(p32(2) + p32(8) + p32(3, endian = "big") + p32(0))
      else:
        print(round(a / b, 2))
        tn.send(p32(2) + p32(8) + p32(2, endian = "big") + struct.pack("f", round(a / b, 2)))
    
  else:
    print("Haha!")
    print(smt + tn.recv())
    break

print(cao)