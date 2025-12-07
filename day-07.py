from functools import cache

grid = [list(x.rstrip()) for x in open(0)]
R, C = len(grid), len(grid[0])

def part1(cs):
    res = 0
    for r in range(1, R-1):
        next_cs = set()
        for c in cs:
            if grid[r+1][c] == '^':
                res += 1
                next_cs.add(c-1)
                next_cs.add(c+1)
            else:
                next_cs.add(c)
        cs = next_cs
    return res

@cache
def part2(r, c):
    if r == R-1: return 1
    if grid[r+1][c] == '^':
        return part2(r+1, c-1) + part2(r+1, c+1)
    else:
        return part2(r+1, c)

sc = grid[0].index('S')
print(part1({sc}))
print(part2(1, sc))
