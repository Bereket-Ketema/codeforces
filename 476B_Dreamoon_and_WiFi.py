from math import pow

def count_ways(idx, pos, target, q):
    if idx == q:
        return 1 if pos == target else 0
    return count_ways(idx+1, pos+1, target, q) + count_ways(idx+1, pos-1, target, q)

s1 = input().strip()
s2 = input().strip()

target = 0
for c in s1:
    if c == '+':
        target += 1
    else:
        target -= 1

current = 0
q = 0
for c in s2:
    if c == '+':
        current += 1
    elif c == '-':
        current -= 1
    else:
        q += 1

favorable = count_ways(0, current, target, q)
total = pow(2, q)

print(f"{favorable/total:.12f}")