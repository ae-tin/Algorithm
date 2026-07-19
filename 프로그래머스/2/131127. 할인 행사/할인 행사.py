def solution(want, number, discount):
    import copy
    answer = 0
    want_dict = dict()
    for w, n in zip(want, number):
        want_dict[w] = n
        
    for i in range(len(discount)-9):
        if set(want) != set(discount[i:i+10]):
            continue
        else:
            tmp_dict = copy.copy(want_dict)
            for j in range(10):
                tmp_dict[discount[i+j]] -= 1
            result = set(list(tmp_dict.values()))
            
            if result == set([0]):
                answer += 1
            else:
                continue
            
    return answer