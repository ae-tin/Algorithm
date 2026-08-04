def solution(scoville, K):
    import heapq
    heapq.heapify(scoville)
    answer = 0
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        m = heapq.heappop(scoville)
        n = heapq.heappop(scoville)
        k = m + (n*2)
        heapq.heappush(scoville, k)
        answer += 1
        
    return answer