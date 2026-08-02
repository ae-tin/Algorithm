def solution(prices):
    from collections import deque
    
    q = deque()
    answer = [0]*len(prices)
    for i, p in enumerate(prices):
        tmp_q = []
        while q:
            j, k = q.popleft()
            if p < k:
                answer[j] = i-j
            else:
                tmp_q.append((j,k))
        q = deque(tmp_q)
        q.append((i,p))
    else:
        while q:
            j, k = q.popleft()
            answer[j] = i-j
    return answer