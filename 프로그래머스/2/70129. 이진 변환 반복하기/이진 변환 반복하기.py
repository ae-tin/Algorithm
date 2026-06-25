def solution(s):
    
    zero = 0
    cnt = 0
    while s != "1":
        ns = ""
        for ss in s:
            if ss == "0":
                zero += 1
            else:
                ns += ss
        s = str(bin(len(ns))[2:])
        cnt += 1
    
    
    answer = [cnt, zero]
    return answer