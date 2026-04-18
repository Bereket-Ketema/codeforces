import bisect

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = sorted(map(int, input().split()))
    
    prev = -10**18
    ok = True
    
    for i in range(n):
        best = float('inf')
        if a[i] >= prev:
            best = min(best, a[i])
        need = prev + a[i]
        idx = bisect.bisect_left(b, need)
        
        if idx < m:
            best = min(best, b[idx] - a[i])
        
        if best == float('inf'):
            ok = False
            break
        
        prev = best
    
    print("YES" if ok else "NO")