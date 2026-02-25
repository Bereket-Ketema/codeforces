for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ans=[]
    
    i=0
    while i<n-1:
        j=0
        while j<n-1-i:
            if b[j]>b[j+1]:
                b[j],b[j+1]=b[j+1],b[j]
                ans.append(f"2 {j+1}")
            j+=1
        i+=1
        
    i=0
    while i<n-1:
        j=0
        while j<n-1-i:
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                ans.append(f"1 {j+1}")
            j+=1
        i+=1
        
    
    for i in range(len(a)):
        if a[i]>b[i]:
            b[i],a[i]=a[i],b[i]
            ans.append(f"3 {i+1}")
            
    print(len(ans))
    for c in ans:
        print(c)
        