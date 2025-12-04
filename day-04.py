grid = [list(s.rstrip()) for s in open(0)]
R, C = len(grid), len(grid[0])
D = [-1, 0, 1]
valid = lambda r, c: 0 <= r < R and 0 <= c < C

def solve(grid, part):
  res = 0
  while True:
    rem = []
    for r in range(R):
      for c in range(C):
        if grid[r][c] != '@': continue
        if sum(valid(r+dy, c+dx) and grid[r+dy][c+dx] == '@' for dy in D for dx in D) < 5:
          rem.append((r, c))
    res += len(rem)
    if part == 1 or len(rem) == 0: break
    for r, c in rem:
      grid[r][c] = '.'

  return res

print(solve(grid, 1))
print(solve(grid, 2))
