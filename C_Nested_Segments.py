n = int(input())
store = []
for _ in range(n):
  store.append(list(map(int,input().split())))
store = [(l, r, i+1) for i, (l, r) in enumerate(store)]
store.sort(key=lambda x: (x[0], -x[1]))

max_ = store[0][1]
max_index = store[0][2]

for i in range(1, n):
  if store[i][1] <= max_:
    print(store[i][2], max_index)
    exit()
  else:
    max_ = store[i][1]
    max_index = store[i][2]
print(-1,-1)