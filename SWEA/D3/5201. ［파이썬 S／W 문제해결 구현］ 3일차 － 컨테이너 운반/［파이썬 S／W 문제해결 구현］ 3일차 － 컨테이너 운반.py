'''
1. 화물의 무게와 트럭의 적재용량을 내림차순으로 sort
2. 적재용량이 큰 첫 번째 트럭부터 무거운 화물의 무게를 싣는다
3. 화물이 매칭되면 다음으로 넘어간다.
예외. 모두 못 싣었으면 return 0
'''
T = int(input())

for test_case in range(1,T+1):
    N, M = map(int, input().split())
    Ws = sorted(list(map(int, input().split())), reverse=True) # N개의 화물의 무게
    Ts = sorted(list(map(int, input().split())), reverse=True) # M개 트럭의 적재용량
    # 모두 싣지 못 할 때
  

    result = 0
    t_idx = 0
    w_idx = 0
    while t_idx != len(Ts) and w_idx != len(Ws):
        # 못 싣으면 다음 트럭과 비교
        if Ts[t_idx] < Ws[w_idx]: 
            w_idx += 1
            continue
        # 싣을 수 있으면 다음 트럭과 다음 화물을 비교
        elif Ts[t_idx] >= Ws[w_idx] :  
            result += Ws[w_idx]
            w_idx += 1
            t_idx += 1

    print(f'#{test_case} {result}')