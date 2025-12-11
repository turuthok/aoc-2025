from collections import defaultdict
from functools import cache

adj = defaultdict(list)
for u, vv in [x.split(": ") for x in open(0).read().splitlines()]:
    adj[u] = vv.split()

@cache
def part_1(u):
    if u == 'out': return 1
    return sum(part_1(v) for v in adj[u])

@cache
def part_2(u, dac, fft):
    if u == 'out': return dac and fft
    return sum(part_2(v, dac or v == 'dac', fft or v == 'fft') for v in adj[u])

print(part_1("you"))
print(part_2("svr", False, False))
