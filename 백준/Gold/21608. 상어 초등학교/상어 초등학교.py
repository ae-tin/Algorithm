dr = [-1, 0, 1, 0] 
dc = [0, 1, 0, -1] # 상 우 하 좌

result = 0
        
N = int(input())    
all_stud = [] # 학생 순서 및 친한친구 담을 리스트
all_stud_dict = {} # 점수 셀 때 딕셔너리가 편함. key: 학생, value: 친구 리스트
for i in range(N ** 2):
    all_stud.append(list(map(int, input().split())))
    all_stud_dict[all_stud[i][0]] = all_stud[i][1:]

seats = [[0] * N for _ in range(N)]

for stud in all_stud:
    
    its_me = stud[0]
    tomodachi = all_stud_dict[its_me]
    
    isiteru_max = 0 # 조건 1 좋아하는 학생이 인접한 칸에 가장 많은 칸을 찾기 위한 변수
    satisfy_1 = [] # 1번 만족하는 자리 담는 리스트
    
    satisfy_2_seats = [] # 조건 2는 한 번에 만족할 수 없음. 1번으로 filtering이 돼야함. 일단 자리 다 담음
    satisfy_2_num = [] # 자리마다 빈자리가 몇 개 인접하는지 담음
    
    for i in range(N):
        for j in range(N):
            if seats[i][j] != 0: # 빈자리가 아니면 볼 필요 없음
                continue
            
            isiteru_num = 0 # 조건 1 좋아하는 학생 세기 위한 변수
            blank_num = 0 # 조건 2 빈 자리 세기 위한 변수
            for k in range(4):
                ni, nj = i + dr[k], j + dc[k]
                if  0 <= ni < N and 0 <= nj < N:
                    if seats[ni][nj] in tomodachi:
                        isiteru_num += 1
                    if seats[ni][nj] == 0 :
                        blank_num += 1
                        
            if isiteru_max == isiteru_num: # 이전의 최대랑 같으면 같이 존재해야함
                satisfy_1.append((i,j))
                isiteru_max = isiteru_num # 그냥 갱신 해봤음
            elif isiteru_max < isiteru_num: # 현재가 더 크면 
                satisfy_1.clear() # 비우고
                satisfy_1.append((i,j)) # 현재만 담음
                isiteru_max = isiteru_num # 갱신
            
            satisfy_2_seats.append((i, j)) # 아직 필터링 전이라 다 담음
            satisfy_2_num.append(blank_num) # 빈자리를
            
    if len(satisfy_1) == 1: # 1번 만족이 유일하면 자리 배정
        i, j = satisfy_1[0]
        seats[i][j] = its_me
    else: 
        tmp_max = 0 # 인접 빈 자리의 최대를 넣을 것
        satisfy_2 = []
        for seat in satisfy_1: # 1번 자리 중
            blank_num = satisfy_2_num[satisfy_2_seats.index(seat)] # 1번 자리의 인접 빈 자리 수
            if tmp_max == blank_num: # 최대랑 같으면 3번으로 넘어갈 여지가 있으니 추가
                satisfy_2.append(seat)
            elif tmp_max < blank_num: # 이전 최대보다 크면 유일할 여지가 있으니 clear 후 추가
                satisfy_2.clear()
                satisfy_2.append(seat)
                tmp_max = blank_num # 갱신
        if len(satisfy_2) == 1: # 2번이 유일하면 자리 앉힘
            i, j = satisfy_2[0][0], satisfy_2[0][1]
            seats[i][j] = its_me
        else: # 아니면 3번 조건
            satisfy_2.sort(key= lambda x: (x[0],x[1])) # 행, 열 기준으로 오름차순
            i, j = satisfy_2[0][0], satisfy_2[0][1] # 0번을 선택하면 그게 조건 만족
            seats[i][j] = its_me

# 채점
for i in range(N):
    for j in range(N):
        stud = seats[i][j] # 본인
        tomodachi = all_stud_dict[stud] # 친한친구
        isiteru_num = 0 # 인접 친구 수
        for k in range(4):
            ni, nj = i + dr[k], j + dc[k]
            if  0 <= ni < N and 0 <= nj < N:
                if seats[ni][nj] in tomodachi:
                    isiteru_num += 1
        confirm = 10 ** (isiteru_num - 1) # 0명 빼고는 10의 거듭제곱들
        if isinstance(confirm, int): # 인접친구가 0이면 int가 아님
            result += confirm
    
print(f'{result}')