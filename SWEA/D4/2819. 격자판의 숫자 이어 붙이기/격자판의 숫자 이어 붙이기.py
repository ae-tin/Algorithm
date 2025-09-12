'''
# 재귀
1. 델타 배열
2. visited 안쓴다
3. 서로 다른 수 -> set
4. 6번 이동 -> how?

종료 조건 : 6번
가지의 수 : 4개(상하좌우)

복잡도 : 16개의 자리에서 상하좌우의 6번의 depth -> 16* 4^6

# BFS 
queue
(0,0,'0')
- (0,1,'0'+'2'), (1,0,'0'+'5') 

'''
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
# 1. 종료조건 : 숫자 7자리 일 때 종료
# 2. 가지의 수 : 4개 (상하좌우)
def recur(y, x, number):
    if len(number) == 7: 
        result.add(number)
        return
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 > ny or ny >= 4 or nx < 0 or nx >= 4: continue

        # 다음 위치로 이동
        recur(ny, nx, number + matrix[ny][nx])



T = int(input())

for test_case in range(1,T+1):
    matrix = [input().split() for _ in range(4)]
    result = set()

    # 7자리 만드는 코드
    # 4 by 4 가 모두 출발점이 될 수 있다
    for sy in range(4):
        for sx in range(4):
            recur(sy, sx, matrix[sy][sx])
    print(f'#{test_case} {len(result)}')