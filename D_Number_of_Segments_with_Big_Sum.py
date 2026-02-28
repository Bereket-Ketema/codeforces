n, s = map(int, input().split())
arr = list(map(int, input().split()))

sums = 0
left = 0
ans = 0
for right in range(n):
  sums += arr[right]

  while sums >= s and left <= right:
    ans += n - right
    sums -= arr[left]
    left += 1

  
print(ans)  