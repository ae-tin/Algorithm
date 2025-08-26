from collections import deque

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    while Q:
        z,x,y,cnt = Q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if data[nz][nx][ny] == 0 and visited[nz][nx][ny] == 0:
                    visited[z][x][y] = 1
                    data[nz][nx][ny] = 1
                    Q.append((nz, nx, ny, cnt+1))

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if data[i][j][k] == 0:
                    return -1
    return cnt


m, n, h = map(int, input().split())
data = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
#pprint(data)
Q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if data[i][j][k] == 1:
                Q.append((i, j, k, 0))
visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
print(bfs())