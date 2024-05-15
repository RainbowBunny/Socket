def f(x, y):
  return 2 * x * y / (x * x + 2 * y * y)

for i in range(-4, 5):
  for j in range(-4, 5):
    if i == 0 and j == 0:
      print("       ", end = "")
      continue
    print(f"{f(i / 10000, j / 10000):.5f} ", end = "")
  print()
