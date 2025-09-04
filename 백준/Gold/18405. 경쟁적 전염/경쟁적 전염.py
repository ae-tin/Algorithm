from collections import deque

def BFS(points,end_s):

    q = deque()
    # 0초 동안 좌표입력, q에 입력되는 
    for i, j, v in points:
        visited[i][j] = True
        q.append((i, j, v, 1))

    while q:
        # while 내부 : s초까지 일어날 일들
        i, j, v, s = q.popleft()
        # s + 1이 시작할 때에 멈춤
        if s == end_s+1: break
        
        for k in range(4):
            r, c = i + dr[k], j + dc[k] # 번질 좌표
            # 범위 내에 있고 방문하지 않았으면 진행
            if 1 <= r <= N and 1 <= c <= N and not visited[r][c] and matrix[r][c] == 0:
                # 방문체크하고 번지는 값 입력
                visited[r][c] = True
                matrix[r][c] = v
                q.append((r, c, v, s+1))
                
N, K = map(int,input().split())
# 0인덱스는 버릴 것. 좌표가 (1,1)부터 시작함
matrix = [ [0]*(N+1) if n == 0 else [0]+ list(map(int,input().split())) for n in range(N+1)]
S, p, q = map(int, input().split()) # S초 후 p,q 좌표의 값?
# 상하좌우 델타를 볼것
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
visited = [[False]*(N+1) for _ in range(N + 1)] # 방문확인할것
start_points = [] # 좌표와 좌표값 저장
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if matrix[i][j] != 0 : start_points.append((i,j,matrix[i][j]))
# 좌표값 순서대로 오름차순정렬
# 혹시 바이러스가 없을 수도 있음
if start_points: 
    start_points.sort(key=lambda x: x[2])
    BFS(start_points, S)

print(matrix[p][q])