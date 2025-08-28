import sys

sys.stdin = open('input.txt', 'r')

import sys
N = int(sys.stdin.readline())

graph = [[]]+ [[i+1 for i,j in enumerate(map(int, sys.stdin.readline().split())) if j == 1] for _ in range(N)]

def dfs(prev,root): # 시작 
    global cnt
    if len(root)==4:
        if root[0] in graph[prev]:
            cnt +=1
            return
    elif len(root) >= 5 :
        return
    else : 
        if graph[prev]:
            for node in graph[prev]:
                if node not in root:
                    root.append(node)
                    dfs(node,root)
                    root.pop()
    
cnt = 0
for prev, edges in enumerate(graph):
    if edges:
        for node in edges:
            dfs(node, [prev,node])
print(cnt)
