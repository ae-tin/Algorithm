T = int(input())
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
for test_case in range(1,T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    visited = [0] * (N*N + 1) # 0인덱스 제외 1번- N^2번 방

    # 현재 위치 숫자 기준 상하좌우 확인
    # 1 큰게 있으면 visited에 1이라고 체크
    for y in range(N):
        for x in range(N):
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]

                if ny < 0 or ny >= N or nx < 0 or nx >= N:
                    continue

                if matrix[ny][nx] == matrix[y][x] + 1:

                    visited[matrix[y][x]] = 1
                    break

    # 연속된 1의 개수가 가장 긴 곳을 찾는다
    # 
    max_cnt = 0 # 정답
    cnt = 0 # 하나하나 마다 몇 개가 연속되는지?
    start = 0 # 숫자 세기 시작한 위치
    for i in range(1, N*N + 1):
        if visited[i] == 1:
            cnt += 1
        else:
            if max_cnt < cnt :
                max_cnt = cnt
                start = i - cnt
            cnt = 0

    print(f'#{test_case} {start} {max_cnt + 1}')