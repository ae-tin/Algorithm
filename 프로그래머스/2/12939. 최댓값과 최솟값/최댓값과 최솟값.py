def solution(s):
    array = list(map(int,s.split()))
    return " ".join([str(min(array)),str(max(array))])