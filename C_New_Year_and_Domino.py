import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

hor = [[0]*m for _ in range(n)]
ver = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m-1):
        if grid[i][j] == '.' and grid[i][j+1] == '.':
            hor[i][j] = 1

for i in range(n-1):
    for j in range(m):
        if grid[i][j] == '.' and grid[i+1][j] == '.':
            ver[i][j] = 1

def build_prefix(mat):
    n = len(mat)
    m = len(mat[0])
    pref = [[0]*(m+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            pref[i][j] = (
                mat[i-1][j-1]
                + pref[i-1][j]
                + pref[i][j-1]
                - pref[i-1][j-1]
            )
    return pref

ph = build_prefix(hor)
pv = build_prefix(ver)

q = int(input())

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())

    h_count = (
        ph[r2][c2-1]
        - ph[r1-1][c2-1]
        - ph[r2][c1-1]
        + ph[r1-1][c1-1]
    )

    v_count = (
        pv[r2-1][c2]
        - pv[r1-1][c2]
        - pv[r2-1][c1-1]
        + pv[r1-1][c1-1]
    )

    print(h_count + v_count)