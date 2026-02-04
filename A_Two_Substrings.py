s = input().strip()

i = s.find("AB")
if i != -1:
    if s.find("BA", i + 2) != -1:
        print("YES")
        exit()

i = s.find("BA")
if i != -1:
    if s.find("AB", i + 2) != -1:
        print("YES")
        exit()

print("NO")
