t = int(input())

for _ in range(t):
    n = int(input())
    a = input().strip()
    b = input().strip()

    ones = 0
    zeros = 0
    balance = []

    for i in range(n):
        if a[i] == '1':
            ones += 1
        else:
            zeros += 1
        balance.append(ones == zeros)

    flipped = False
    possible = True

    for i in range(n-1, -1, -1):

        cur = a[i]

        if flipped:
            cur = '1' if cur == '0' else '0'

        if cur == b[i]:
            continue

        if not balance[i]:
            possible = False
            break

        flipped = not flipped

    if possible:
        print("YES")
    else:
        print("NO")