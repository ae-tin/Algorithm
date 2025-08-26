import sys

sys.stdin = open('input (1).txt', 'r')

M, N, H = map(int,input().split())
matrix = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]

dh = [-1, 1, 0, 0, 0, 0]
dr = [0, 0, -1, 1, 0, 0]
dc = [0, 0, 0, 0, 1, -1]

day = 0
cnt_0 = 0
chk = 0
while True:
    day += 1 
    for h in range(H):
        for n in range(N):
            for m in range(M):
                clear = [1]*6
                if matrix[h][n][m] == 1:
                    for k in range(6):
                        if 0<=h+dh[k]<H and 0<=n+dr[k]<N and 0<=m+dc[k]<M:
                            if matrix[h+dh[k]][n+dr[k]][m+dc[k]] == 0:
                                matrix[h+dh[k]][n+dr[k]][m+dc[k]] = 1
                        else : continue
                elif day == 1 and matrix[h][n][m] == 0:
                    cnt_0 += 1
                    for k in range(6):
                        if 0<=h+dh[k]<H and 0<=n+dr[k]<N and 0<=m+dc[k]<M:
                            if matrix[h+dh[k]][n+dr[k]][m+dc[k]] == -1:
                                clear[k] = 0
                        else : clear[k] = 0
                else : continue
                if sum(clear) == 0 and day == 1:
                    chk = 1
                    break
    
    if day == 1:
        if cnt_0 == 0 :
            print('-1')
            break
        if chk == 1:
            print('-1')
            break
    # break
    green_tomato = 0

    for h in range(H):
        for n in range(N):
            for m in range(M):
                if matrix[h][n][m] == 0 : green_tomato += 1
    if green_tomato == 0 : 
        print(f'{day}')
        break
