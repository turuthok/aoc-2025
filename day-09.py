p = []
for line in open(0).read().splitlines():
    x, y = map(int, line.split(','))
    p.append((x, y))
n = len(p)

def calc(p1, p2):
    x1, x2 = min(p1[0], p2[0]), max(p1[0], p2[0])
    y1, y2 = min(p1[1], p2[1]), max(p1[1], p2[1])
    return (x2-x1+1) * (y2-y1+1)

print(max(calc(p[i], p[j]) for i in range(n) for j in range(i+1, n)))

xset = {-1, 1_000_000} # make a coordinate that's extreme min and max
yset = {-1, 1_000_000}
for pp in p:
    xset.add(pp[0])
    yset.add(pp[1])

def compress(s):
    l, d = [], {}
    for value in sorted(s):
        d[value] = len(l)
        l.append(value)
    return l, d

px, xx = compress(xset)
py, yy = compress(yset)
R, C = len(py), len(px)

grid = [['.'] * C for _ in range(R)]

p.append(p[0])

for i, pp in enumerate(p):
    x, y = pp
    p[i] = xx[x], yy[y]

for i in range(n):
    x1, y1 = p[i]
    x2, y2 = p[i+1]

    dy = y2-y1; dx = x2-x1
    if dy < 0: dy = -1
    if dy > 0: dy = 1
    if dx < 0: dx = -1
    if dx > 0: dx = 1

    while (x1, y1) != (x2, y2):
        grid[y1][x1] = '#'
        x1 += dx; y1 += dy

q = [(0, 0)]
for r, c in q:
    for rr, cc in [(r+1, c), (r-1, c), (r, c-1), (r, c+1)]:
        if 0 <= rr < R and 0 <= cc < C and grid[rr][cc] == '.':
            grid[rr][cc] = 'x'
            q.append((rr, cc))

def valid(p1, p2):
    x1, x2 = min(p1[0], p2[0]), max(p1[0], p2[0])
    y1, y2 = min(p1[1], p2[1]), max(p1[1], p2[1])
    for y in range(y1, y2+1):
        for x in range(x1, x2+1):
            if grid[y][x] == 'x': return False
    return True

def orig(pp):
    x, y = pp
    return px[x], py[y]

print(max(calc(orig(p[i]), orig(p[j])) for i in range(n) for j in range(i+1, n) if valid(p[i], p[j])))
