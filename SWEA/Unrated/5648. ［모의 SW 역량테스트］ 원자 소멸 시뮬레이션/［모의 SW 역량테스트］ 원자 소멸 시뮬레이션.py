def dist(A_point, B_point): # (x,y,d) d: 상하좌우 0123 
    ar, ac, ad = A_point
    br, bc, bd = B_point
    # 처음 거리, 1초 후 거리
    return abs(ar-br) + abs(ac-bc), abs((ar + dx[ad]*0.5) - (br + dx[bd]*0.5)) + abs((ac + dy[ad]*0.5) - (bc + dy[bd]*0.5))
def N_seconds_after(A_point, B_point): # (x,y,d) d: 상하좌우 0123
    A_point, B_point = sorted([A_point, B_point], key = lambda x: x[2]) # d로 정렬하면 A포인트가 상또는 하
    ar, ac, ad = A_point
    br, bc, bd = B_point
    # 같은 방향은 만날 수 없음
    if ad == bd : return False, False, False
    # 6가지 경우 (상하01 상좌02 상우03 하좌12 하우13 좌우23)
    elif set([ad, bd]) == set([0, 1]): 
        if ar != br: return False, False, False
        else:
            cross_point = (ar, round((ac + bc)/2 if int((ac + bc)/2) != (ac + bc)/2 else int((ac + bc)/2), 1), 4)
            current_dista, after1_dista =  dist(A_point, cross_point)
            current_distb, after1_distb =  dist(B_point, cross_point)
            if current_dista > after1_dista and current_distb > after1_distb and current_dista == current_distb : 
                return True, cross_point, current_dista
            else : return False, False, False
    elif set([ad, bd]) == set([2, 3]): 
        if ac != bc: return False, False, False
        else:
            cross_point = (round((ar + br)/2, 1) if int((ar + br)/2) != (ar + br)/2 else int((ar + br)/2), ac, 4)
            current_dista, after1_dista =  dist(A_point, cross_point)
            current_distb, after1_distb =  dist(B_point, cross_point)
            if current_dista > after1_dista and current_distb > after1_distb and current_dista == current_distb : 
                return True, cross_point, current_dista
            else : return False, False, False
    elif set([ad, bd]) in [set([0, 2]), set([0, 3]), set([1, 2]), set([1, 3])]: 
        cross_point = (ar, bc, 4)
        current_dista, after1_dista =  dist(A_point, cross_point)
        current_distb, after1_distb =  dist(B_point, cross_point)
        if current_dista > after1_dista and current_distb > after1_distb and current_dista == current_distb : 
            return True, cross_point, current_dista
        else: return False, False, False


T = int(input())

dy = [1, -1, 0, 0, 0]
dx = [0, 0, -1, 1, 0] # 상하좌우 정지

for test_case in range(1,T+1):

    N = int(input())

    atoms = [tuple(list(map(int, input().split()))) for _ in range(N)] # x, y, d, E
    future_dict = dict() # key : 몇 초 후 터지는지 , value: dict -> key: 터지는 좌표, value: 터질 원자 좌표 두개 쌍을 담은 리스트 
    boom_set = set() # 터질 법한 좌표들 모두

    for i in range(N-1): # 좌표들의 조합
        x1, y1, d1, e1 = atoms[i]
        for j in range(i+1, N):
            x2, y2, d2, e2 = atoms[j]
            is_boom, cross_point, n_seconds = N_seconds_after((x1, y1, d1),(x2, y2, d2)) # 터지는 지 여부, 교차하는 좌표, 몇 초 후 터지는 지
            if is_boom: # 터지는 거면
                future_dict.setdefault(n_seconds, dict()).setdefault(cross_point,list()).append([(x1, y1, e1),(x2, y2, e2)]) # 좌표쌍 저장
                boom_set.add((x1, y1, e1)) # 터질 후보군 set에 저장
                boom_set.add((x2, y2, e2)) # 터질 후보군 set에 저장

    total_energy = 0 # 결과값 초기화
    future_dict_key_sort = sorted(list(future_dict.keys()))# 먼저 터지는 순으로 key 정렬
    for s in future_dict_key_sort: # 터지는 초 빠른순으로 순회
        for xys in future_dict[s].keys(): # 그 초에 터질 좌표들. 중복 매우 존재
            tmp_union_set = set() # 중복 제거를 위한 set
            for point1, point2 in future_dict[s][xys]: # 좌표 쌍이 
                if point1 in boom_set and point2 in boom_set: # 터질 후보군에 둘 다 존재하면
                    tmp_union_set.add(point1) # 중복 제거할 거야
                    tmp_union_set.add(point2)
                elif point1 in boom_set or point2 in boom_set: # 만약 한개만 boom set에 있는건 이미 터진거니까 패스
                    continue
            for point in tmp_union_set: # 중복제거한 좌표들의 에너지를 더함
                total_energy += point[2]
            boom_set = boom_set - tmp_union_set # 전체 후보군 set에서 그 초에 터질 좌표들 제거

    print(f'#{test_case} {total_energy}')