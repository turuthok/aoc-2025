def valid(x, part):
  s = str(x)
  n = len(s)

  if part == 1:
    if n % 2 != 0: return True
    start = n // 2
  else:
    start = 1

  for l in range(start, n // 2 + 1):
    if n % l != 0: continue
    prefix = s[:l]
    if prefix * (n // l) == s: return False
  return True

def solve(s, part):
  res = 0
  for intv in s.split(','):
    a, b = map(int, intv.split('-'))
    while a <= b:
      if not valid(a, part):
        res += a
      a += 1
  return res

s = input()
print(solve(s, 1))
print(solve(s, 2))
