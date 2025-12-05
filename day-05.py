first, second = open(0).read().rstrip().split('\n\n')

from collections import defaultdict

count = defaultdict(int)
intvs = []
for intv in first.split('\n'):
    a, b = map(int, intv.split('-'))
    count[a] += 1
    count[b+1] -= 1
    intvs.append((a, b+1))

res = 0
for x in map(int, second.split('\n')):
    res += any(a <= x < b for a, b in intvs)
print(res)

res = curr = 0
for x in sorted(count.keys()):
    if curr > 0:
        res += x - last
    curr += count[x]
    last = x
print(res)

