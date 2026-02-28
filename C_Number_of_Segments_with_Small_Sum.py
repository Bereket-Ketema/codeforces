n, s = map(int, input().split())
arr = list(map(int, input().split()))

length = 0
left = 0
current = 0
for right in range(n):
  current += arr[right]

  while current > s and left <= right:
    current -= arr[left]
    left += 1

  if current <= s:
    length += (right - left + 1)
  
print(length)  