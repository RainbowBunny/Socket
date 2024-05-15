from pwn import *

tn = connect("112.137.129.129", 27001)
tn.send(p32(0) + p32(8) + b"22021105")

while True:
  smt = (tn.recv())
  if smt[0] == 1:
    a = int.from_bytes(smt[8 : 12], "little")
    b = int.from_bytes(smt[12 : 16], "little")
    tn.send(p32(2) + p32(4) + p32(a + b))
  else:
    print(smt)
    break