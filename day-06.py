import math

def calc(arr, op):
    if op == '+':
        return sum(arr)
    else:
        return math.prod(arr)

*orig_arr, ops = open(0).read().splitlines()
ops = ops.split()

arr = [list(map(int, x.split())) for x in orig_arr]
arr = list(zip(*arr))  # flip the array (mirror based on main diagonal)
print(sum(calc(x, y) for x, y in zip(arr, ops)))

arr = list(zip(*orig_arr))[::-1]                   # easier to transpose the matrix counter clockwise
arr = list(map(lambda x: ''.join(x).strip(), arr)) # then combine into strings, each calculation will be
                                                   # delimited by empty string element.

res = 0
curr = []
for x in arr:
    if not x:
        res += calc(curr, ops.pop())
        curr = []
    else:
        curr.append(int(x))
res += calc(curr, ops.pop())
print(res)
