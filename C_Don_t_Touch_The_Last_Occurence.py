#third-first
#ICPC_C_BEREKET-KETEMA
n=int(input())
num=list(map(int,input().split()))
num.reverse()
print(len(set(num)))
for i in range(n):
  for j in range(i+1,n):
    if num[i]==num[j]:
      num[j]="#"
num.reverse()
for i in num:
  if i!="#":
    print(i,end=" ")