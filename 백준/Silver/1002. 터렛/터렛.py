T = int(input())

for tc in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    square_dist_turret = (x1 - x2)**2 + (y1 - y2)**2
    if (x1, y1) == (x2, y2) and r1 == r2:
        result = -1
    elif (x1, y1) == (x2, y2) and r1 != r2:
        result = 0
    elif square_dist_turret == (r1 + r2)**2:
        result = 1
    elif square_dist_turret == (r1 - r2)**2:
        result = 1
    elif square_dist_turret > (r1 + r2)**2:
        result = 0
    elif square_dist_turret < (r1 - r2)**2:
        result = 0
    elif square_dist_turret < (r1 + r2)**2:
        result = 2
    print(result)