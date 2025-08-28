import sys
sys.stdin = open('input.txt', 'r')
N = int(sys.stdin.readline())

graph = [[]]+ [[i+1 for i,j in enumerate(map(int, sys.stdin.readline().split())) if j == 1] for _ in range(N)]

cnt = 0
for node1 in range(1,N+1):
    for node2 in graph[node1]:
        if node1 != node2:
            for node3 in graph[node2]:
                if node3 != node1 and node3 != node2:
                    for node4 in graph[node3]:
                        if node4 != node1 and node4 != node2 and node4 != node3:
                            for node5 in graph[node4]:
                                if node5 == node1:
                                    cnt +=1
                                else: continue
                        else: continue
                else: continue
        else: continue

print(cnt)
