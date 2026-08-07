def solution(order):
    L = list(range(len(order), 0, -1))
    s = []
    answer = 0

    for o in order:
        if s and s[-1] == o:
            s.pop()
            answer += 1
            continue

        while L and L[-1] != o:
            s.append(L.pop())

        if L and L[-1] == o:
            L.pop()
            answer += 1
        else:
            break

    return answer