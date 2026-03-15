t = int(input())

for _ in range(t):
    
    n = int(input())
    R = list(map(int, input().split()))
    
    m = int(input())
    B = list(map(int, input().split()))
    
    max_r = 0
    cur = 0
    
    for x in R:
        cur += x
        max_r = max(max_r, cur)
    
    max_b = 0
    cur = 0
    
    for x in B:
        cur += x
        max_b = max(max_b, cur)
    
    print(max_r + max_b)