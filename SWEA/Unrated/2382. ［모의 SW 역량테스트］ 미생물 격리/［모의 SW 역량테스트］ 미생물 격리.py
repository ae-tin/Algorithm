from collections import deque


dr = [0, -1, 1, 0, 0] # 상 하 좌 우
dc = [0, 0, 0, -1, 1]
        
T = int(input())

for testcase in range(1,T+1):
    N, M, K = map(int, input().split())
    cluster = [tuple(map(int, input().split())) for _ in range(K)]
    cluster.sort(key=lambda x: x[2], reverse=True)
    # print(cluster)
    # matrix[i][j]를 리스트로 만들어서 미생물 군집을 넣을 것
    matrix = [[[] for _ in range(N)] for _ in range(N)]
    ud = set([1,2])
    lr = set([3,4])
    T = 1
    while T != M+1:
        # 단순히 좌표만 갱신 후 matrix에 저장. 이미 방향과 군집수는 바뀌어 있어야함
        for k in range(len(cluster)):
            i, j, m, d = cluster[k]
            ni, nj = i + dr[d], j + dc[d]
            matrix[ni][nj].append((ni, nj, m, d))
        else:
            cluster.clear()
        

        # matrix 돌면서 1. 합칠 군집 확인 2. 약품에 있는 군집 확인
        for i in range(N):
            for j in range(N):
                C = matrix[i][j]
                # 군집 없으면 패스
                if not C: 
                    continue
                # 약품이 아니면
                if i not in [0, N-1] and j not in [0, N-1]:
                    # 군집이 여러개이면 (약품에서는 두 군집이 만날 수 없다)
                    if len(C) > 1:
                        # 가장 많은 미생물 군집 방향을 따름
                        # print((i,j),C, T)
                        d = C[0][3]
                        m = sum([c[2] for c in C])
                        cluster.append((i, j, m, d))
                        matrix[i][j].clear()
                    else: 
                        cluster.append(C[0])
                        matrix[i][j].clear()
                # 약품이면
                else:
                    r, c, m, d = C[0]
                    # 미생물 몫 0이면 군집 없앰
                    if m // 2 == 0: 
                        matrix[i][j].clear()
                        continue
                    else: m //= 2
                    # 방향전환
                    if d in ud:
                        a = ud - set([d])
                        d = list(a)[0]
                    elif d in lr:
                        a = lr - set([d])
                        d = list(a)[0]
                    cluster.append((r, c, m, d))
                    matrix[i][j].clear()
        
        cluster.sort(key=lambda x: x[2],reverse=True)
        T += 1

    result = sum([ c[2] for c in cluster])

    print(f'#{testcase} {result}')