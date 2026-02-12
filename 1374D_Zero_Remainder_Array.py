from collections import defaultdict
 
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    remains = defaultdict(int)
 
    for i in nums:
        remain = k - (i % k)
        if remain % k == 0:
            continue
        
        remains[remain] += 1
 
    max_ = 0
    for ke in remains:
        val = ke + (remains[ke] - 1) * k
        max_ = max(max_, val)
    if remains:
        print(max_ + 1)
    else:
        print(0)