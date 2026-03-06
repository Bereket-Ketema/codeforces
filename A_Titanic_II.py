#third-first
#ICPC_C_BEREKET-KETEMA
n=input()
k=int(input())
num=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
m=num.index(n)+k
def chk(m):
  if m>=12:
    m-=12
    return chk(m)
  return m
print(num[chk(m)])