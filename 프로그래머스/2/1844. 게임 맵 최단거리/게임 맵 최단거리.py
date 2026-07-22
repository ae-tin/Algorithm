def solution(maps):
    answer = -1
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    n, m = len(maps), len(maps[0])
    q = []
    # 시작점 삽입, 끝점 = (n-1,m-1)
    q.append((0,0,1))
    maps[0][0] = 0
    
    while q:
        x, y, k = q[0]
        q.pop(0)
        
        if x == n-1 and y == m-1:
            answer = k
            break
            
        for r, c in zip(dr,dc):
            nx, ny = x+r, y+c
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1:
                    
                    maps[nx][ny] = 0
                    q.append((nx,ny,k+1))
                    # visited[nx][ny] = True
        
    return answer