def solution(n, stations, w):
    from collections import deque
    answer = 0
    stations = deque(stations)
    need_station = []
    coverage = w*2 + 1
    prev_station, prev_right = 0, 0
    final_station = n
    while stations:
        cur_station = stations.popleft()
        cur_left, cur_right = cur_station - w - 1, cur_station + w
        # 계산
        left_coverage = cur_left - prev_right
        if left_coverage > 0:
            s, k = divmod(left_coverage, coverage)
            answer += s
            if k > 0:
                answer += 1
            need_station.append(left_coverage)
        # 마지막 처리
        if not stations:
            right_coverage = n - cur_right
            if right_coverage > 0:
                s, k = divmod(right_coverage, coverage)
                answer += s
                if k > 0:
                    answer += 1
                need_station.append(right_coverage)
        
        prev_right = cur_right
    
    return answer