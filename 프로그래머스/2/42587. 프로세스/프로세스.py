def solution(priorities, location):
    answer = 1
    sorted_p = sorted(priorities, reverse=True)
    
    while priorities:
        
        if sorted_p[0] == priorities[0]:
            sorted_p.pop(0)
            priorities.pop(0)
            if location == 0:
                return answer
            else:
                location -= 1
                answer += 1
        else:
            priorities = priorities[1:] + [priorities[0]]
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
    
    return answer