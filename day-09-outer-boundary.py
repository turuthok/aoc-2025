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

def normalize_dir(value):
    if value < 0: return -1
    if value > 0: return 1
    return 0

def get_dir(p1, p2):
    return normalize_dir(p2[0]-p1[0]), normalize_dir(p2[1]-p1[1])

def cross(ax, ay, bx, by, cx, cy):
    return (ax-cx) * (by-cy) - (bx-cx) * (ay-cy)

a = min(range(n), key=lambda i: (p[i][1], p[i][0]))
outer = [(p[a][0]-1, p[a][1]-1)]
for _ in range(n-1):
    pa = p[a % n]; pb = p[(a+1) % n]; pc = p[(a+2) % n]
    dx, dy = get_dir(pa, pb)
    turn = cross(*pa, *pb, *pc)
    if turn < 0:
        if dx:
            outer.append((pb[0]-dx, outer[-1][1]))
        else:
            outer.append((outer[-1][0], pb[1]-dy))
    else:
        if dx:
            outer.append((pb[0]+dx, outer[-1][1]))
        else:
            outer.append((outer[-1][0], pb[1]+dy))
    a += 1
outer.append(outer[0])

def overlap(p1, p2, p3):
    return p3[0] >= min(p1[0], p2[0]) and p3[0] <= max(p1[0], p2[0]) and p3[1] >= min(p1[1], p2[1]) and p3[1] <= max(p1[1], p2[1])

def intersects(p1, p2, p3, p4):
    o1 = cross(*p1, *p2, *p3)
    o2 = cross(*p1, *p2, *p4)
    o3 = cross(*p3, *p4, *p1)
    o4 = cross(*p3, *p4, *p2)
    if o1 * o2 < 0 and o3 * o4 < 0:
        return True

    if o1 == 0 and overlap(p1, p2, p3): return True
    if o2 == 0 and overlap(p1, p2, p4): return True
    if o3 == 0 and overlap(p3, p4, p1): return True
    if o4 == 0 and overlap(p3, p4, p2): return True

    return False

def intersects_outer(p1, p2):
    for i in range(n):
        if intersects(p1, p2, outer[i], outer[i+1]):
            return True
    return False

def valid(p1, p2):
    x1, x2 = min(p1[0], p2[0]), max(p1[0], p2[0])
    y1, y2 = min(p1[1], p2[1]), max(p1[1], p2[1])

    return not (intersects_outer((x1, y1), (x2, y1)) or intersects_outer((x2, y1), (x2, y2)) or intersects_outer((x2, y2), (x1, y2)) or intersects_outer((x1, y2), (x1, y1)))

print(max(calc(p[i], p[j]) for i in range(n) for j in range(i+1, n) if valid(p[i], p[j])))
