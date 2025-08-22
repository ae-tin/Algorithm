def in_traverse(n): # 전위순회,,!
    global result # 결과 가져옴
    global tree
    if tree[n]: # 자식 노드가 존재하면
        in_traverse(tree[n][0]) # 왼쪽 자식 노드 순회
        result.append(letter[n]) # 다돌았으면 자신의 문자 추가
        if len(tree[n]) == 2:  # 오른쪽 자식 노드가 존재하면
            in_traverse(tree[n][1]) # 순회
    else : result.append(letter[n]) # 리프노드면 문자 추가

T = 10#int(input())
for test_case in range(1, 1+T):
    N = int(input())
    infos = [[]]+[list(input().split()) for _ in range(N)]
    letter = [0]+[lst[1] for lst in infos[1:]]
    tree = [[]]+[list(map(int,list(lst[2:]))) if len(lst)>2 else [] for lst in infos[1:]]
    
    result = []
    in_traverse(1)
    print(f'#{test_case} {"".join(result)}')