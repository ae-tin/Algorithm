def solution(n):
    import copy
    a, b = 0, 1
    cnt = 1
    while n >= cnt:
        answer = a + b
        b = copy.copy(a)
        a = copy.copy(answer)
        cnt += 1
    
    return answer%1234567