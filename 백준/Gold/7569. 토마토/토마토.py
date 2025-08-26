from collections import deque
def bfs(info_q):
    global matrix
    global visited
        
    while info_q:
        depth, h, n, m = info_q.popleft()
        matrix[h][n][m] = depth
        for k in range(6):
            nh, nn, nm = h+dh[k], n+dr[k], m+dc[k]
            if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M and visited[nh][nn][nm]==False and matrix[nh][nn][nm]==0:
                visited[nh][nn][nm] = True
                info_q.append((depth+1,nh,nn,nm))
            
    cnt_0 = 0
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if matrix[h][n][m] == 0 : cnt_0 += 1
    if cnt_0 == start_num:
        return depth
    else : return -1


M, N, H = map(int,input().split())
matrix = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False]*M for _ in range(N)] for _ in range(H)]

dh = [-1, 1, 0, 0, 0, 0]
dr = [0, 0, -1, 1, 0, 0]
dc = [0, 0, 0, 0, 1, -1]

red_tomatoes = deque()
for h in range(H):
    for n in range(N):
        for m in range(M):
            if matrix[h][n][m] == 1: 
                red_tomatoes.append((0,h,n,m))
                visited[h][n][m] = True
start_num = len(red_tomatoes)
print(bfs(red_tomatoes))