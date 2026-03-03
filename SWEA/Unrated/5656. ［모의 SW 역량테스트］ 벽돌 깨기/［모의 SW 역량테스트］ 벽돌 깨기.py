import copy

def cleanup(matrix):
    cnt = 0
    for w in range(W):
        col = [x for x in matrix[w] if x != 0]
        cnt += len(col)
        matrix[w] = col + [0] * (H - len(col))
    return matrix, cnt


T = int(input())
for test_case in range(1,T+1):
    
    N, W, H = map(int,input().split())
    
    bricks_tmp = [list(map(int,input().split())) for _ in range(H)]
    bricks = []
    for w in range(W):
        tmp = []
        for h in range(H):
            tmp.append(bricks_tmp[H-1-h][w])
        bricks.append(tmp)
    
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    result_cnt = W * H
    
    def bfs(bricks_copy,points):
        q = []
        q.append(points)
        
        while q:
            a,b = q.pop()
            boom = bricks_copy[a][b]
            if boom == 0:
                continue
            bricks_copy[a][b] = 0
            for i in range(1, boom):
                for k in range(4):
                    na, nb = a + dr[k]*i, b + dc[k]*i
                    if na < 0 or na >= W or nb < 0 or nb >= H:
                        continue
                    next_node = bricks_copy[na][nb]
                    if next_node != 0:
                        q.append((na,nb))
        return cleanup(bricks_copy)
        
    
    def dfs(depth, bricks_copy):
        global result_cnt
        bp = False
        if depth == N : 
            _, cnt = cleanup(copy.deepcopy(bricks_copy))
            result_cnt = min(result_cnt, cnt)
            return
        if result_cnt == 0 : return
        
        for w in range(W):
            hit = None
            for h in range(H-1, -1, -1):
                if bricks_copy[w][h] != 0:
                    hit = (w,h)
                    break
            
            if hit is None: 
                
                dfs(depth + 1, copy.deepcopy(bricks_copy))
            else:
                next_board = copy.deepcopy(bricks_copy)
                next_board, cnt = bfs(next_board, hit)
                result_cnt = min(result_cnt, cnt)
                dfs(depth + 1, next_board)
    dfs(0, copy.deepcopy(bricks))
    
    
    print(f"#{test_case} {result_cnt}")