n, k = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
freq = {}

best_l = 0
best_r = 0

for right in range(n):

    freq[arr[right]] = freq.get(arr[right], 0) + 1

    while len(freq) > k:
        freq[arr[left]] -= 1

        if freq[arr[left]] == 0:
            del freq[arr[left]]

        left += 1

    if right - left > best_r - best_l:
        best_l = left
        best_r = right

print(best_l + 1, best_r + 1)