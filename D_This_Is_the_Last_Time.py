t = int(input())

for _ in range(t):
  store = []
  n, k = map(int, input().split())
  for _ in range(n):
    store.append([int(i) for i in input().split()])
  store.sort()

  for num in store:
    if k >= num[0] and k <= num[1]:
      k = max(k, num[2])
  print(k)
