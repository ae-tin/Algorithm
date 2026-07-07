def solution(s):
    stack = []
    
    for ss in s:
        if ss == "(":
            stack.append(ss)
        else:
            if not stack:
                stack.append(ss)
            elif stack[-1] == "(":
                stack.pop()
    if not stack:
        return True
    else:
        return False