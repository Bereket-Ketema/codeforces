def check(time):
    left = coord_speed[0][0] - coord_speed[0][1] * time
    right = coord_speed[0][0] + coord_speed[0][1] * time

    for i in range(1, n):
        pos = coord_speed[i][0]
        speed = coord_speed[i][1]

        new_left = pos - speed * time
        new_right = pos + speed * time

        # No intersection
        if new_left > right:
            return False

        # Update intersection
        left = max(left, new_left)
        right = min(right, new_right)

    return True


n = int(input())
coord = list(map(int, input().split()))
speeds = list(map(int, input().split()))

coord_speed = list(zip(coord, speeds))
coord_speed.sort()

low = 0
high = 1e9

for _ in range(100): 
    mid = (low + high) / 2
    if check(mid):
        high = mid
    else:
        low = mid

print(f"{high:.6f}")