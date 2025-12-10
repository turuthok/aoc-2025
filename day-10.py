import re
from scipy.optimize import linprog

def presses(buttons, lights):
    for m in range(1, 1 << len(buttons)):
        l = 0
        for i, button_mask in enumerate(buttons):
            if m & (1 << i):
                l ^= button_mask
        if l == lights:
            yield m

part_1 = part_2 = 0

for lights, *buttons, counts in [x.split() for x in open(0).read().splitlines()]:
    lights = sum(1 << (i-1) for i in range(len(lights)) if lights[i] == '#')
    buttons = list(map(lambda b: sum(1 << int(x) for x in re.findall(r"\d+", b)), buttons))
    counts = list(map(int, re.findall(r"\d+", counts)))

    N = len(counts)
    V = len(buttons)

    part_1 += min(x.bit_count() for x in presses(buttons, lights))

    c = [1] * V
    bounds=[(0, None)] * V
    equations = [[0] * V for _ in range(N)]
    for i in range(N):
        for j in range(V):
            if buttons[j] & (1 << i):
                equations[i][j] = 1

    part_2 += int(linprog(c, A_eq=equations, b_eq=counts, bounds=bounds, integrality=c).fun)

print(part_1)
print(part_2)
