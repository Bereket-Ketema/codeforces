n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

one = 0
store = []

for two in range(m):
    while one < n and arr1[one] < arr2[two]:
        one += 1
    store.append(one)

print(*store)