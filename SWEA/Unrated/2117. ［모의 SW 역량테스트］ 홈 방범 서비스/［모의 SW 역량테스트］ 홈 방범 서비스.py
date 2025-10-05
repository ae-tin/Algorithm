from collections import deque


dr = [1, 0, -1, 0] # 하 우 상 좌
dc = [0, 1, 0, -1]

def main_fee(K): # K 영역마다 운영 비용
    return K * K + (K - 1) * (K - 1)

def bfs(start_point, K, visited, M):
    global result # 최종 결과 갱신
    q = deque()
    # 큐에 들어가기 전에 방문처리
    i,j = start_point
    visited[i][j] = True
    q.append((K, start_point))
    
    profit = 0
    current_K = K # K가 바뀔때 요금 계산할 것
    
    while q:
        K, (r, c) = q.popleft()
        # 종료조건 1. 모든 영역을 탐색했을 때 2. result에 모든 집이 기록 됐을 때
        if K == 2 * N or result == house_points : break
        # K가 바뀌면 요금 계산 후 result 갱신
        if current_K != K:
            if main_fee(current_K) - profit <= 0 : 
                result = max(profit//M, result)
            current_K = K
        # 집이 영역 내에 있으면 이익 계산
        if matrix[r][c] == 1: profit += M
        # 다음 영역 탐색
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((K + 1, (nr, nc)))
    # 끝났을 때 한 번 더 갱신
    if main_fee(current_K) - profit <= 0 : 
        result = max(profit//M, result)
        

    
T = int(input())

for testcase in range(1,T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    house_points = 0 # 집포인트 개수 기록
    result = 1
    # 집 포인트 개수 기록
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1: house_points += 1
    # 전체 순회
    for i in range(N):
        for j in range(N):
            visited = [[False]*N for _ in range(N)]
            bfs((i,j), 1, visited, M)

    print(f'#{testcase} {result}')