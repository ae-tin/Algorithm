
def in_traverse(n): # 중위순회,,!, 노드에서 위치 받아옴
    global result # 결과 가져옴
    global tree
    if tree[n]: # 자식 노드가 존재하면
        if len(tree[n]) == 2:  # 오른쪽 자식 노드가 존재하면
            result.append('(')
            in_traverse(tree[n][0]) # 왼쪽 자식 노드 순회
            result.append(letter[n]) # 다돌았으면 자신의 문자 추가
            in_traverse(tree[n][1]) # 순회
            result.append(')')
        else :
            print('s')
    else : result.append(letter[n]) # 리프노드면 문자 추가

def calculator(evalutaion):
    stack = []
    evalutaion = evalutaion[::-1]
    for s in evalutaion:
        if s == ')': stack.append(s)
        elif s.isdecimal() : stack.append(s)
        elif s in '+-*/' : stack.append(s)
        elif s == '(':
            cal = 0
            while True:
                pop = stack.pop()
                if pop.isdigit(): 
                    cal += int(pop)
                elif pop in '+-*/':
                    cal2 = stack.pop()
                    if pop == '+' and cal2.isdigit():
                        cal += int(cal2)
                    elif pop == '-' and cal2.isdigit():
                        cal -= int(cal2)
                    elif pop == '*' and cal2.isdigit():
                        cal *= int(cal2)
                    elif pop == '/' and cal2.isdigit():
                        cal //= int(cal2)
                elif pop == ')': break
            stack.append(str(cal))
    return int(stack[0])

T = 10#int(input())
for test_case in range(1, 1+T):
    N = int(input())
    infos = [[]]+[list(input().split()) for _ in range(N)]
    letter = [0]+[lst[1] for lst in infos[1:]]
    tree = [[]]+[list(map(int,list(lst[2:]))) if len(lst)>2 else [] for lst in infos[1:]]
    
    result = []
    in_traverse(1)
    print(f'#{test_case} {calculator(result)}')