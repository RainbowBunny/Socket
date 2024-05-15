from pwn import *
from Crypto.Util.number import GCD

tn = connect("112.137.129.129", 27012)
tn.send(b'0 8 22021105')

def factorial(n: int) -> int:
  ans = 1
  for i in range(1, n + 1):
    ans *= i 
  return ans

while True:
  smt = tn.recv()
  print(smt)
  if smt[0] == 49:
    tom = list(map(int, smt.split(b' ')))[3:]
    m = {}
    for e in tom:
      if not e in m:
        m[e] = 1
      else:
        m[e] += 1
    ans = factorial(len(tom))
    print(len(tom))
    for e in m:
      print(e, m[e])
      ans //= factorial(m[e])
    tn.sendline(b'2 4 ' + str(ans).encode())
    print(ans)
  else:
    print('Huhu')
    break