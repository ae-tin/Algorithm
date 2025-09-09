T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    M = N//2
    all_carot = list(map(int, input().split()))
    carot_set = sorted(list(set(all_carot)))
    # 크기는 1에서 30, 인덱스로 접근
    cnt_carot = [0]*31 
    for k in all_carot:
        cnt_carot[k] += 1
    categorize = [[],[],[]]
    result = 1000
    for i in range(N-2): # 소 그룹의 끝 인덱스 [0,i]
        for j in range(i+1,N-1): # 중 그룹의 끝 인덱스 [i+1, j] # 대 그룹 인덱스 [j+1:]
            # 당근 개수 확인
            s = sum([ cnt_carot[k] for k in carot_set[:i+1]])
            m = sum([ cnt_carot[k] for k in carot_set[i+1:j+1]])
            l = sum([ cnt_carot[k] for k in carot_set[j+1:]])
            # 당근 개수 차이 확인 N//2보다 작아야함. 아니면 다음
            if max([s,m,l]) > M or min([s,m,l]) == 0: continue
            diff = max([s,m,l]) - min([s,m,l])
            result = min([result, diff])
    if result == 1000: result = -1
            
    print(f'#{test_case} {result}')