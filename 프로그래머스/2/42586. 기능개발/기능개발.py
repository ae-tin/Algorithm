def solution(progresses, speeds):
    # 작업 시간
    work_days = [0]*len(speeds)
    for i, (p, s) in enumerate(zip(progresses, speeds)):
        work_day = (100 - p)/s
        if work_day != int(work_day):
            work_day = int(work_day) + 1
        work_days[i] = int(work_day)
    work_days += [101]
    print(work_days)
    answer = []
    done_idx, tmp_done, peak_day = 1, 1, work_days[0]
    while done_idx <= len(speeds):
        if work_days[done_idx] <= peak_day:
            done_idx += 1
            tmp_done += 1
        else:
            answer.append(tmp_done)
            tmp_done = 1
            peak_day = work_days[done_idx]
            done_idx += 1
            
            
    return answer

# progresses = [83, 4, 5, 2, 1, 99]
# speeds = [1, 3, 5, 6, 2, 1]
# print(solution(progresses,speeds))