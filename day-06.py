import math
from itertools import groupby

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

arr = list(zip(*orig_arr))[::-1]                      # easier to transpose the matrix counter clockwise
arr = list(map(lambda x: ''.join(x).strip(), arr))    # then combine into strings, each calculation will be

# group the subarrays delimited by empty string element
arr = [list(group) for key, group in groupby(arr, key=bool) if key]
arr = [list(map(int, x)) for x in arr]
print(sum(calc(x, y) for x, y in zip(arr, ops[::-1])))
