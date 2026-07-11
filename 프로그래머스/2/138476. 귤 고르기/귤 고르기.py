# def solution(k, tangerine):
#     cnt = dict()
#     for i in tangerine:
#         cnt[i] = cnt.setdefault(i, 0) + 1
#     cnt = sorted(list(cnt.values()), reverse=True)
#     for j in range(1, len(cnt)+1):
#         if k <= sum(cnt[:j]):
#             return j
def solution(k, tangerine):
    answer = 0
    check = 0
    tangerine.sort()
    dup = {}
    for i in tangerine:
        if i in dup:
            dup[i] += 1
        else:
            dup[i] = 1

    arr = sorted(dup.items(), key=lambda x: x[1], reverse=True)
    if arr[0][1] >= k:
        return 1
    else:
        for i in arr:
            if check < k:
                check += i[1]
                answer += 1
            else:
                break
    return answer