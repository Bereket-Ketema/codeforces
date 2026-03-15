t = int(input())

for _ in range(t):
    n, l, r = map(int, input().split())
    arr = list(map(int, input().split()))

    left = {}
    right = {}

    for i in range(l):
        c = arr[i]
        left[c] = left.get(c, 0) + 1

    for i in range(l, n):
        c = arr[i]
        right[c] = right.get(c, 0) + 1

    for c in list(left.keys()):
        if c in right:
            m = min(left[c], right[c])
            left[c] -= m
            right[c] -= m
            l -= m
            r -= m

    if l < r:
        left, right = right, left
        l, r = r, l

    ans = 0
    diff = l - r

    for c in left:
        pairs = left[c] // 2
        use = min(pairs, diff // 2)

        ans += use
        left[c] -= use * 2
        diff -= use * 2

    ans += diff // 2

    remaining = sum(left.values()) + sum(right.values())

    ans += remaining // 2

    print(ans)