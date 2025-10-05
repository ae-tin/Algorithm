
from collections import deque

T = int(input())

for testcase in range(1,T+1):
    N, M, K, A, B = map(int, input().split())
    Ai = list(map(int, input().split()))
    Ai_dict = {i: {'T':Ai[i] , 'process': deque()} for i in range(N)}
    Bi = list(map(int, input().split()))
    Bi_dict = {i: {'T':Bi[i] , 'process': deque()} for i in range(M)}
    Ti = list(map(int, input().split()))[::-1] # pop할거라 뒤집어서 시간 최소화

    result = -1
    max_time = K*max(Ai)*max(Bi)
    waiting_A = deque()
    waiting_B = deque()
    A_set = set()
    B_set = set()
    n = 1
    for t in range(max_time+1):
        # waiting for A
        while True: # 손님왔다 받아라
            if Ti and Ti[-1] == t: 
                Ti.pop()
                waiting_A.append(n) # 고객번호
                n += 1
            else: break            
            
        # A 창구 입장
        # 빈 A가 있으면 넣는다
        for i in range(N):
            # 다 처리한 사람은 나오고 B waiting 입장
            if Ai_dict[i]['process']:
                if Ai_dict[i]['process'][0][0] == t:
                    _, cus = Ai_dict[i]['process'].popleft()
                    waiting_B.append(cus)
            # 빈 A가 있으면 넣는다
            if not Ai_dict[i]['process'] and waiting_A:
                Ai_dict[i]['process'].append((t + Ai_dict[i]['T'], waiting_A.popleft())) # 나올 시간 기록
                if i == A-1: A_set.add(Ai_dict[i]['process'][0][1])
             
        # waiting for B
        for i in range(M):
            if Bi_dict[i]['process']:
                if Bi_dict[i]['process'][0][0] == t:
                    _, cus = Bi_dict[i]['process'].popleft()
            # 빈 A가 있으면 넣는다
            if not Bi_dict[i]['process'] and waiting_B:
                Bi_dict[i]['process'].append((t + Bi_dict[i]['T'], waiting_B.popleft())) # 나올 시간 기록
                if i == B-1: B_set.add(Bi_dict[i]['process'][0][1])
        
    
    inter_set = A_set.intersection(B_set)
    if inter_set:
        result += 1 + sum(inter_set)

    print(f'#{testcase} {result}')