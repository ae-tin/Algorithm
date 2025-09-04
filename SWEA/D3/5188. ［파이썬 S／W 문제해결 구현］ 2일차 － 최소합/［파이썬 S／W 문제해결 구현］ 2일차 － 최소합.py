def DFS(point, s):
    global min_v
    i, j = point
    # 중간에 합이 더 크면 리턴
    if s >= min_v: return
    # 마지막 좌표면 리턴
    elif (i,j) == (N-1,N-1): 
        min_v = min([min_v, s]) 
        return  
    
    for k in range(2):
        r, c = i + dr[k], j + dc[k]
        if 0 <= r < N and 0 <= c < N:
            DFS((r, c), s + matrix[r][c])
    
T = int(input())

for test_case in range(1,T+1):

    N = int(input())
    # 오른쪽이나 아래만 다닌다
    dr = [1, 0]
    dc = [0, 1]

    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 최소값 갱신
    min_v = 1e9
    # 현재좌표까지 합도 같이 넘겨준다
    DFS((0,0),matrix[0][0])
    print(f'#{test_case} {min_v}')

