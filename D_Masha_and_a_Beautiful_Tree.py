import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        
        def dfs(l, r):
            if r - l == 1:
                return 0
            
            mid = (l + r) // 2
            left = dfs(l, mid)
            right = dfs(mid, r)
            
            if left == -1 or right == -1:
                return -1

            if max(arr[l:mid]) < min(arr[mid:r]):
                return left + right

            if max(arr[mid:r]) < min(arr[l:mid]):
                arr[l:mid], arr[mid:r] = arr[mid:r], arr[l:mid]
                return left + right + 1
            
            return -1
        
        res = dfs(0, len(arr))
        print(res)

solve()