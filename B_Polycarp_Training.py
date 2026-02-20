n = int(input())
store = [ int(_) for _ in input().split()]
store.sort()
k = 1
ans = 0
for i in store:
  if i >= k:
    ans = k
    k += 1
print(ans)