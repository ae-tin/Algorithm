def solution(topping):
    if len(topping) == 1: return 0
    answer = 0
    a = dict()
    b = dict()
    for t in topping:
        b[str(t)] = b.setdefault(str(t),0) + 1
    for t in topping:
        a[str(t)] = a.setdefault(str(t),0) + 1
        b[str(t)] -= 1
        if b[str(t)] == 0:
            del b[str(t)]
        if len(a.keys()) == len(b.keys()):
            answer += 1
        
    return answer