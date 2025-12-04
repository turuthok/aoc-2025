def solve(arr, picks):
  res = 0
  for s in arr:
    value = 0
    for rem in range(picks, 0, -1):
      prefix_len = len(s) - (rem-1)  # can only pick from this prefix
      p = max(s[:prefix_len])        # pick the biggest number greedily
      idx = s.find(p)                # pick the earliest occurrence of that number
      s = s[idx+1:]                  # the remaining string to operate for next iterations
      value = value * 10 + int(p)

    res += value
  return res

arr = [s.rstrip() for s in open(0)]
print(solve(arr, 2))
print(solve(arr, 12))
