def DFS(current_node, path, depth, s):
    global min_v
    # 중간에 합이 더 크면 리턴
    if s >= min_v: return
    # 마지막 depth면 리턴
    elif depth == N: 
        # 마지막 노드에서 첫 노드까지 더해줌
        s += matrix[current_node][0]
        min_v = min([min_v, s]) 
        return  
    # 0은 시작점이므로 돌지 않음
    for next_node in range(1,N):
        if next_node not in path:
            path[depth] = next_node
            DFS(next_node, path, depth+1, s + matrix[current_node][next_node])
            path[depth] = 0
    
T = int(input())

for test_case in range(1,T+1):

    N = int(input())
    # 오른쪽이나 아래만 다닌다
    dr = [1, 0]
    dc = [0, 1]

    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 최소값 갱신
    min_v = 1e9
    # 사용한 노드
    used = [0]*N
    # 현재좌표까지 합도 같이 넘겨준다
    DFS(0, used, 1, 0)
    print(f'#{test_case} {min_v}')