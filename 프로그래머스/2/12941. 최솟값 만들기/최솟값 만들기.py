def solution(A,B):
    answer = 0
    for a, b in zip(sorted(A), sorted(B)[::-1]):
        answer += a*b
    return answer