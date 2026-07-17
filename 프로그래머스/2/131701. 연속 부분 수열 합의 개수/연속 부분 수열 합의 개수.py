def solution(elements):
    n = len(elements)
    answer = set()
    tmp_circle = elements * 2
    for i in range(n):
        for j in range(1, n+1):
            answer.add(sum(tmp_circle[i:i+j]))
    
    return len(answer)