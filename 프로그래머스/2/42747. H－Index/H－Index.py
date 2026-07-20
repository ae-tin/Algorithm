def solution(citations):
    citations.sort()
    answer = [0]
    n = len(citations)
    # if citations[0] > n: return n
    for i, c in enumerate(citations):
        k = n - i # h편이상
        if c >= k:
            answer.append(min(c,k))
    return max(answer)

# c = [4, 4, 4, 4, 4, 4] #4
# c = [0, 1, 5, 2] #2
# c = [10, 9, 8, 6] #4
# c = [0] #0
# c = [3, 4] #2
# c = [1, 2, 3, 5, 6, 7, 10, 11] #5
# c = [3, 5, 11, 6, 1, 5, 3, 3, 1, 41] #5
# c = [1, 11, 111, 1111] #3
# print(solution(c))