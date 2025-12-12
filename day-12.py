from itertools import groupby
import re

def rotate(rows):
    return list(''.join(x) for x in zip(*rows[::-1]))

*shapes, regions = [list(group) for key, group in groupby(open(0).read().splitlines(), key=bool) if key]

K = 3 # assume all pattern is 3 x 3

all_shapes = []
all_sizes = []
for shape in shapes:
    rows = shape[1:]
    s = set()
    for _ in range(4):
        s.add(tuple(rows))
        rows = rotate(rows)

    for i, x in enumerate(rows):
        rows[i] = rows[i][::-1]

    for _ in range(4):
        s.add(tuple(rows))
        rows = rotate(rows)

    all_shapes.append(s)
    all_sizes.append(sum(x.count('#') for x in rows))

def put(r, c, shape, grid):
    for i in range(K):
        for j in range(K):
            if shape[i][j] == '#' and grid[r+i][c+j] == '#': return False

    for i in range(K):
        for j in range(K):
            if shape[i][j] == '#':
                grid[r+i][c+j] = '#'

    return True

def remove(r, c, shape, grid):
    for i in range(K):
        for j in range(K):
            if shape[i][j] == '#':
                grid[r+i][c+j] = '.'

def go(idx, rem, grid, seen):
    if idx == len(rem): return 1
    if rem[idx] == 0: return go(idx+1, rem, grid, seen)

    key = ''.join(''.join(x) for x in grid)
    if key in seen: return 0
    seen.add(key)

    for r in range(R):
        if r+K > R: break
        for c in range(C):
            if c+K > C: break
            for shape in all_shapes[idx]:
                if put(r, c, shape, grid):
                    rem[idx] -= 1
                    res = go(idx, rem, grid, seen)
                    rem[idx] += 1
                    remove(r, c, shape, grid)
                    if res: return 1
    return 0

res = 0
for region in regions:
    C, R, *rem = map(int, re.findall(r'\d+', region))
    if sum(all_sizes[i] * cnt for i, cnt in enumerate(rem)) > R * C: continue
    res += go(0, rem, [['.'] * C for _ in range(R)], set())

print(res)
