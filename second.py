def f(n):
  for x in range(n):
    yield x**3

for x in f(6):
  print (x)

# -----------The above code will gives the following output----------

# 0
# 1
# 8
# 27
# 64
# 125
