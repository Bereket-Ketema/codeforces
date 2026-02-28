n, s = map(int, input().split())
store = list(map(int, input().split()))

left = 0
current = 0
max_len = 0

for right in range(n):
  current += store[right]

  while current > s:
    current -= store[left]
    left += 1
  max_len = max(max_len, right - left + 1)

print(max_len)
