store = []
row, column = 0, 0
for i in range(5):
  mat = list(map(int,input().split()))
  if 1 in mat:
    row = i
  store.append(mat)

for i in range(5):
  if store[row][i] == 1:
    column = i
    break
print(abs(2 - row)+abs(2-column))