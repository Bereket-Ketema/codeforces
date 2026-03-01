from collections import Counter
n = int(input())
for _ in range(n):
    haystack = input()
    needle = input()
    freq_hay = Counter(haystack)
    freq_needle = Counter(needle)

    skip_outer = False

    for k, v in freq_hay.items():
      if v > freq_needle.get(k, 0):
        print("Impossible")
        skip_outer = True
        break
    if skip_outer:
      continue

    for ch in freq_hay:
      if ch in freq_needle:
          remove_count = min(freq_needle[ch],freq_hay[ch])
          freq_needle[ch] -= remove_count
          if freq_needle[ch] == 0:
              del freq_needle[ch]

    l_needle = []
    for ch in freq_needle:
        l_needle.extend([ch] * freq_needle[ch])

    l_needle.sort()


    result = ''
    l = 0
    for i, num in enumerate(l_needle):
      if l < len(haystack) and num < haystack[l]:
        result += num
      else:
        while l < len(haystack) and num >= haystack[l]:
          result += haystack[l]
          l += 1
        result += num
    result += haystack[l:]
    print(result)
