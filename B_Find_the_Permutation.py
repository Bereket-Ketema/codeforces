from functools import cmp_to_key

def solve():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        adj = [input().strip() for _ in range(n)]
        
        p = list(range(1, n + 1))
        
        def compare(u, v):
            if u < v:
                return -1 if adj[u-1][v-1] == '1' else 1
            else:
                return 1 if adj[v-1][u-1] == '1' else -1

        p.sort(key=cmp_to_key(compare))
        print(*p)

solve()