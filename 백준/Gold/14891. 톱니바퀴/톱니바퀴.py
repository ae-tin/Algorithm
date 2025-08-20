
matrix = [list(map(int,list(input()))) for _ in range(4)]
K = int(input())
howtoturn = [tuple(map(int, input().split())) for _ in range(K)]

def turn(lst, direction):
    '''
    turn 함수 : 톱니 1개를 방향에 따라 회전 시키는 함수
    시계 방향인경우 오른쪽 마지막 톱니가 왼쪽 앞으로 들어옴
    반시계 방향의 경우 왼쪽 마지막 톱니가 오른쪽 마지막으로 들어옴
    '''
    if direction == 1: lst.insert(0, lst.pop(-1)) # 시계 방향
    elif direction == -1: lst.append(lst.pop(0)) # 반시계
    
    return lst


def which_direction(now, now_direction):
    '''
    바로 옆 인접 톱니 확인
    인덱스가 범위를 벗어나도 return하긴 함
    하지만 direction을 예외인 -2로 처리하면서 함수 밖에서 예외처리 할 예정
    '''
    global matrix
    global visited
    left_right = [ now + i if 0 <= now + i <= 3 else -1 for i in [-1, 1]]
    direc = []
    for idx in left_right:
        if idx == -1 or visited[idx] == 1:
            direc.append(-2)
        elif idx < now and visited[idx] == 0: 

            if matrix[now][-2] == matrix[idx][2]: direc.append(0)
            else: direc.append(-now_direction)

        elif idx > now and visited[idx] == 0:

            if matrix[now][2] == matrix[idx][-2]:
                direc.append(0)
            else: direc.append(-now_direction)

        else: pass

    return [(left_right[0], direc[0]), (left_right[1], direc[1])]


def bfs(now, direction):
    '''
    bfs 함수
    모든 톱니를 방문했을 때 종료함
    '''
    global visited
    global matrix
    if sum(visited) == 4: return
    else:
        idx_directions = which_direction(now, direction)
        idx_directions.sort(key = lambda x : -x[0])

        if direction != 0 and visited[now] == 0:
            matrix[now] = turn(matrix[now], direction)

        visited[now] = 1

        for n_idx, n_direction in idx_directions:
            if n_direction == -2 :continue
            bfs(n_idx, n_direction)



for n, direction in howtoturn:
    now_idx = n-1
    visited = [0]*4
    bfs(now_idx, direction)

result = 0
weight = 0
for mat in matrix:
    if mat[0] == 1:
        result += 2**weight
    weight += 1

print(result)