
from collections import deque


dr = [1, 0, -1, 0] # 하 우 상 좌
dc = [0, 1, 0, -1]

def main_fee(K):
    return K * K + (K - 1) * (K - 1)

def bfs(start_point, K, visited, M):
    global result
    q = deque()
    q.append((K, start_point))
    i,j = start_point
    visited[i][j] = True
    profit = 0
    current_K = K
    
    while q:
        K, (r, c) = q.popleft()
        if K == 2 * N or result == start_points : break
        
        if current_K != K:
            if main_fee(current_K) - profit <= 0 : 
                result = max(profit//M, result)
            current_K = K

        if matrix[r][c] == 1: profit += M

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((K + 1, (nr, nc)))
    if main_fee(current_K) - profit <= 0 : 
        result = max(profit//M, result)
        

    
T = int(input())

for testcase in range(1,T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    start_points = 0
    result = 1
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1: start_points += 1
    for i in range(N):
        for j in range(N):

            visited = [[False]*N for _ in range(N)]
            bfs((i,j), 1, visited, M)

    print(f'#{testcase} {result}')