from pwn import *
import time
from Crypto.Util.number import isPrime

tn = connect("112.137.129.129", 27015)
tn.send(p32(0) + p32(8) + b'22021105')

print(tn.recv())