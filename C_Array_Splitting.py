n, k = map(int,input().split())
store = [int(_) for _ in input().split()]
if len(store) == k:
  print(0)
  exit()
elif k == 1:
  print(store[-1] - store[0])
  exit()
gaps = []
for i in range(1, n):
  gaps.append(store[i] - store[i-1])
gaps.sort(reverse=True)
total = store[-1] - store[0]
for i in range(k-1):
  total -= gaps[i]
print(total)