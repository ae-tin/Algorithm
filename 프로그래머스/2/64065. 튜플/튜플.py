def solution(s):
    
    input_list = s.lstrip("{").rstrip("}").split("},{")
    tuple_list = []
    for t in input_list:
        tuple_list.append(list(map(int,t.split(","))))
            
    tuple_list.sort(key=lambda x: len(x))
    answer = []
    for i, li in enumerate(tuple_list):
        if i==0:
            answer.append(li[0])
            prev = set(li)
        else:
            answer.append(list(set(li) - prev)[0])
            prev = set(li)
    return answer