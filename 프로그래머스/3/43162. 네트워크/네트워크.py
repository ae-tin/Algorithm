def solution(n, computers):
    # 연결이 되있더라도 작은 수 노드를 부모로 보고 부모 루트를 네트워크 인덱스로 생각한다
    # 전체 노드의 부모 루트 개수를 찾자
    # 일단 부모는 자기 자신으로 초기화
    answer = set()
    parent = [i for i in range(n)]
    def find_parent(x):
        # 부모 찾기 함수
        nonlocal parent
        
        if parent[x] != x:
            parent[x] = find_parent(parent[x])
        return parent[x]
    
    def union(x, y):
        # x, y를 같은 네트워크로 합치는 함수
        nonlocal parent
        
        root_x = find_parent(x)
        root_y = find_parent(y)
        if root_x < root_y:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y
    
    for i, node in enumerate(computers):
        for j in range(i+1, n):
            if computers[i][j] == 1:
                if find_parent(i) != find_parent(j):
                    union(i,j)
    
    for i in range(n):
        answer.add(find_parent(i))
    
        
        
    return len(answer)