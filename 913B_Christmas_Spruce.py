import sys
input = sys.stdin.readline

n = int(input())

children = [[] for _ in range(n + 1)]

for i in range(2, n + 1):
    p = int(input())
    children[p].append(i)

for i in range(1, n + 1):
    if len(children[i]) == 0:
        continue
    
    leaf_children = 0
    
    for child in children[i]:
        if len(children[child]) == 0:
            leaf_children += 1
    
    if leaf_children < 3:
        print("No")
        exit()

print("Yes")