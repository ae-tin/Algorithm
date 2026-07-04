def solution(dirs):
    # 좌표를 2배 늘려서 변을 중간 좌표로 생각
    d = {
        "U":[0,2],
        "D":[0,-2],
        "L":[-2,0],
        "R":[2,0],
    }
    answer = 0
    matrix = [ [0]*22 for _ in range(22)]
    x, y, cum_x, cum_y = 0, 0, 0, 0
    for s in dirs:
        dx, dy, markx, marky = d[s][0], d[s][1], d[s][0]//2, d[s][1]//2
        cum_x, cum_y = cum_x + dx, cum_y + dy
        if cum_x > 10 or cum_x < -10 or cum_y > 10 or cum_y < -10:
            cum_x, cum_y = cum_x - dx, cum_y - dy
            continue
        mark_x, mark_y = x + markx, y + marky
        x, y = x + dx, y + dy
        matrix[mark_x][mark_y] += 1
    
    for i in range(22):
        for j in range(22):
            if matrix[i][j] > 0 :
                answer += 1
    return answer