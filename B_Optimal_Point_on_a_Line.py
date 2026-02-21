n = int(input())
store = [int(_) for _ in input().split()]
store.sort()
if len(store) % 2 != 0:
  print(store[len(store) // 2])
else:
  print(store[(len(store) // 2)-1])
