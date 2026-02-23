n, t = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
first, second = 0, 0

store = []
while first < len(arr1) and second < len(arr1):
  if arr1[first] <= arr2[second]:
    store.append(arr1[first])
    first += 1
  else:
    store.append(arr2[second])
    second += 1

store.extend(arr1[first:])
store.extend(arr2[second:])

print(*store)