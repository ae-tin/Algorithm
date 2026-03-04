#import sys
#sys.stdin = open("sample_input.txt", "r")


T = int(input())
for test_case in range(1,T+1):
    
    N, M = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    
    max_boom = 0
    
    for n in range(N):
        for m in range(M):
            tmp_boom = matrix[n][m]
            K = matrix[n][m]
            for k in range(1, K+1):
                for i in range(4):
                    nn, nm = n + k*dr[i], m + k*dc[i]
                    if 0<=nn<N and 0<=nm<M:
                        tmp_boom += matrix[nn][nm]
            max_boom = max(tmp_boom, max_boom)
            
    print(f"#{test_case} {max_boom}")