def solution(skill, skill_trees):
    from copy import copy
    answer = 0
    skill_set = set(list(skill))
    skill_order = list(skill[::-1])
    for sk in skill_trees:
        order_tmp = copy(skill_order)
        drop = False
        for s in sk:
            if s in skill_set:
                if order_tmp[-1] == s:
                    order_tmp.pop()
                else:
                    drop = True
            else:
                pass
        else:
            if not drop:
                answer += 1
                
    return answer