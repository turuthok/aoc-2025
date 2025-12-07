from functools import cache
from collections import defaultdict

grid = [list(x.rstrip()) for x in open(0)]
R, C = len(grid), len(grid[0])
cc = {grid[0].index('S'): 1}

splits = 0
for r in range(1, R-1):
    next_cc = defaultdict(int)
    for c, w in cc.items():
        if grid[r+1][c] == '^':
            splits += 1
            next_cc[c-1] += w
            next_cc[c+1] += w
        else:
            next_cc[c] += w
    cc = next_cc

print(splits)
print(sum(cc.values()))
