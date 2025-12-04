N = 100

def solve(cmds, part):
  pos = N // 2
  res = 0
  for cmd in cmds:
    steps = int(cmd[1:]) * (1 if cmd[0] == 'R' else -1)
    next_pos = pos + steps

    if part == 2:
      if next_pos >= N:
        res += next_pos // N 
      elif next_pos <= 0:
        res += (1 if pos > 0 else 0) + (-next_pos) // N

    pos = next_pos % N

    if part == 1:
      res += pos == 0
  return res

cmds = list(open(0))
print(solve(cmds, 1))
print(solve(cmds, 2))
