arr = [list(map(int, x.split(','))) for x in open(0)]
n = len(arr)

def dist(i, j):
    return sum((arr[i][k]-arr[j][k]) ** 2 for k in range(3))

data = []
for i in range(n):
    for j in range(i+1, n):
        data.append((dist(i, j), i, j))

g = list(range(n))
m = [[i] for i in range(n)]
rem = n

for iters, (d, i, j) in enumerate(sorted(data), 1):
    gi = g[i]; gj = g[j]
    if gi != gj:
        rem -= 1
        if rem == 1:
            part2 = arr[i][0] * arr[j][0]

        m[gi].extend(m[gj])
        for idx in m[gj]:
            g[idx] = gi
        m[gj] = []

    if iters == 1000:
        part1 = 1
        for idx in sorted(range(n), key=lambda x: len(m[x]), reverse=True)[:3]:
            part1 *= len(m[idx])

print(part1)
print(part2)

