t = int(input())
for _ in range(t):
    n, x, k = map(int, input().split())
    s = input().strip()
    
    post = 0
    first = -1
    cycle = -1
    
    for i in range(n):
        post += 1 if s[i] == 'R' else -1
        
        if first == -1 and x + post == 0:
            first = i + 1
        
        if cycle == -1 and post == 0:
            cycle = i + 1

    if first == -1 or first > k:
        print(0)
    elif cycle == -1:
        print(1)
    else:
        print(1 + (k - first) // cycle)