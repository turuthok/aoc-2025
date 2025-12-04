def invalid(s):
  n = len(s)
  for l in range(1, n // 2 + 1):
    if n % l != 0: continue
    if s[:l] * (n // l) == s:
      return True
  return False

def solve(s, part):
  res = 0
  for intv in s.split(','):
    a, b = map(int, intv.split('-'))
    for pre in range(1, b+1):
      s = str(pre)
      if invalid(s): continue   # we only want prime prefixes

      # generate all multiples of this prefix that are <= b
      t = s + s
      value = int(t)
      if value > b: break
      while value <= b:
        if value >= a:
          res += value

        t += s
        if part == 1:
          t += s
        value = int(t)
  return res

s = input()
print(solve(s, 1))
print(solve(s, 2))
