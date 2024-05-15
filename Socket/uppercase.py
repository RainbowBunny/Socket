from pwn import *

tn = connect("112.137.129.129", 27017)
tn.send(p32(0) + p32(8) + b"22021105")

while True:
  smt = (tn.recv())
  
  if smt[0] == 1:
    ln = int.from_bytes(smt[4:8], "little")
    ss = ""
    for i in range(ln):
      ss += chr(smt[i+8])
    print(ss.upper())

    tn.send(p32(2) + p32(ln) + ss.upper().encode())
  else:
    print("Hmm...")
    print(smt)
    break