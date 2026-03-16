import sys

input = sys.stdin.read
data = input().split()

index = 0
t = int(data[index])
index += 1

for _ in range(t):
    n = int(data[index])
    index += 1
    
    a = []
    for i in range(n):
        a.append(int(data[index]))
        index += 1
    
    ans = 0
    for k in range(2, n):
        mx_out = a[n-1]
        thresh = max(mx_out - a[k], a[k]) + 1
        
        left = 0
        right = k - 1
        
        while left < right:
            if a[left] + a[right] >= thresh:
                ans += right - left
                right -= 1
            else:
                left += 1
    
    print(ans)