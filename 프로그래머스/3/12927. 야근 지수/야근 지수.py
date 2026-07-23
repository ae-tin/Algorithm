def solution(n, works):
    if sum(works) <= n:
        return 0

    work_dict = {}

    for w in works:
        work_dict[w] = work_dict.get(w, 0) + 1

    max_work = max(work_dict.keys())

    while n > 0 and max_work > 0:
        count = work_dict.get(max_work, 0)

        if count == 0:
            max_work -= 1
            continue

        move = min(n, count)

        work_dict[max_work] -= move
        work_dict[max_work - 1] = work_dict.get(max_work - 1, 0) + move
        n -= move

        if work_dict[max_work] == 0:
            del work_dict[max_work]
            max_work -= 1

    answer = 0
    for work, count in work_dict.items():
        answer += (work ** 2) * count

    return answer