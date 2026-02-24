#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    if N <= M : 
        A = list(map(int,input().split()))
        B = list(map(int,input().split()))
    else:
        B = list(map(int,input().split()))
        A = list(map(int,input().split()))
    
    sum_max = -1e-9
    for j in range(len(B)-len(A)+1):
        tmp_sum = 0
        for i in range(len(A)):
            tmp_sum += A[i]*B[j+i]
        else:
            sum_max = max(sum_max, tmp_sum)
    print(f'#{test_case} {sum_max}')
    