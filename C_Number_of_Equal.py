from collections import Counter
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

freq = Counter(b)
check = 0
for num in a:
  if num in freq:
    check += freq[num]

print(check)