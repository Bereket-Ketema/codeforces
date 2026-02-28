t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    word = input()
    
    whites = word[:k].count('W')
    ans = whites
    
    for i in range(k, n):
        
        if word[i - k] == 'W':
            whites -= 1
        
        if word[i] == 'W':
            whites += 1
        
        ans = min(ans, whites)
    
    print(ans)