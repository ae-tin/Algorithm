def solution(str1, str2):
    mul_col1, mul_col2 = set(), set()
    
    for idx in range(len(str1)-1):
        if str1[idx].isalpha() and str1[idx+1].isalpha():
            s1 = str1[idx:idx+2].lower()
            while True:
                if s1 in mul_col1:
                    s1 += '.'
                else:
                    mul_col1.add(s1)
                    break
        else:
            continue
            
    for idx in range(len(str2)-1):
        if str2[idx].isalpha() and str2[idx+1].isalpha():
            s2 = str2[idx:idx+2].lower()
            while True:
                if s2 in mul_col2:
                    s2 += '.'
                else:
                    mul_col2.add(s2)
                    break
        else:
            continue
            
    if not mul_col1 and not mul_col2:
        return 65536
    answer = len(mul_col1.intersection(mul_col2))/len(mul_col1.union(mul_col2)) 
    return int(answer*65536)