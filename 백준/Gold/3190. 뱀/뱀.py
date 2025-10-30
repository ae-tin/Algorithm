from collections import deque
"""
    초계산을 우째해야하나?
"""
dr = [0, 1, 0, -1] 
dc = [1, 0, -1, 0] # 우 하 좌 상
        
N = int(input())    
K = int(input()) 
apples = set([tuple(map(int, input().split())) for _ in range(K)])
L = int(input()) 
rotates = [tuple(input().split()) for _ in range(L)]
d_dict = {'D':5,'L':3}
d = 0 # 방향
wall = [0, N + 1]

snake = deque()
snake.append((1,1))
T = 1
while True :
    
    i, j = snake[-1]
    ni, nj = i + dr[d], j + dc[d]
    
    if ni in wall or nj in wall or (ni, nj) in snake:
        break
    
    snake.append((ni, nj))
    
    if (ni, nj) in apples: 
        apples.discard((ni, nj))
    else: 
        snake.popleft()
        
    if rotates and int(rotates[0][0]) == T:
        d = (d + d_dict[rotates[0][1]]) % 4
        rotates.pop(0)
        
    T += 1

print(f'{T}')