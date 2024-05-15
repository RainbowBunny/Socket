from pwn import *
from Crypto.Util.number import GCD

tn = connect("112.137.129.129", 27012)
tn.send(p32(0) + p32(8) + p32(22021105))

while True:
  smt = (tn.recv())
  print(smt)
  if smt[0] == 1:
    print("hmm")
    print(smt)
  else:
    # print(smt + tn.recv())
    break