def solution(n):
    cnt = bin(n)[2:].count("1")
    k = 0
    while k != cnt:
        n += 1
        k = bin(n)[2:].count("1")
    return n