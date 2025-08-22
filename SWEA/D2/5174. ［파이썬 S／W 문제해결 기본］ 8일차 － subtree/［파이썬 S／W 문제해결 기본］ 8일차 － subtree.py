def pre_traverse(n):
    global start
    global result
    result += 1
    if tree[n]:
        for node in tree[n]:
            pre_traverse(node)

T = int(input())
for test_case in range(1, 1+T):
    edge, start = map(int, input().split())
    edges = list(map(int, input().split()))
    tree = [[] for _ in range(max(edges)+1)]
    for i in range(len(edges)//2):
        s_idx, leaf = edges[i*2], edges[i*2+1] 
        tree[s_idx].append(leaf)
    result = 0
    pre_traverse(start)
    print(f'#{test_case} {result}')