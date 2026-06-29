def test(s):
    s_dict = {
        "}":"{",
        "]":"[",
        ")":"(",
    }
    stack = []
    for ch in s:
        if ch in ["(", "{", "["]:
            stack.append(ch)
        else: 
            if stack:
                if stack[-1] == s_dict[ch]:
                    stack.pop()
            else:
                return False
            
    if stack:
        return False
    else:
        return True
    
def solution(s):
    answer = 0
    n = len(s)
    for _ in range(n):
        
        if test(s):
            answer += 1
        tmp = list(s)
        tmp = tmp[1:] + [tmp[0]]
        s = ''.join(tmp)
    
    return answer