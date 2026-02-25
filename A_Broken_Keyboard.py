n = int(input())
for _ in range(n):
  s = input()
  left, right = 0, 1

  if len(s) == 1:
    print(s)
    continue
  
  store = set()

  while right < len(s):
    if s[left] == s[right]:
      left += 2
      right += 2
      continue
    store.add(s[left])
    left += 1
    right += 1
  store.add(s[left:])
  store = list(store)
  store.sort()
  print(''.join(store))
