T = int(input())

for test_case in range(1,T+1):
    a, b, c = map(int, input().split())

    result = 0
    
    # 다 만족했으면 탈출
    # if a < b and b < c : pass
    # 뒤에서부터 먹는 게 좋을 것 같음
    if b < c : pass
    else : 
        result += b-c+1
        b = c - 1
        
    if a < b : pass
    else : 
        result += a-b+1
        a = b - 1
    # 안되는 케이스
    if a < 1 or b < 2 or c < 3 :
        result = -1
        
    print(f'#{test_case} {result}')