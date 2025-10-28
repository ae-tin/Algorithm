from collections import deque

"""
1. bfs로 섬 군집 개수 세기
2. 가로 세로 가능한 다리 찾기 
3. 다리 조합 dfs로 최소 다리 길이 찾기
"""
N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs(i, j, prev):  # prev 섬 index
    global visited, matrix
    """
    섬일때만 처리
    matrix의 섬에 인덱스 부여
    """
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    matrix[i][j] = prev + 1
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni, nj = i + dr[k], j + dc[k]
            if (
                0 <= ni < N
                and 0 <= nj < M
                and not visited[ni][nj]
                and matrix[ni][nj] == 1
            ):
                visited[ni][nj] = True
                matrix[ni][nj] = prev + 1
                q.append((ni, nj))
    return prev + 1


visited = [[False] * M for _ in range(N)]
prev_idx = 0  # 버리는 섬 인덱스
island_set = set()  # 섬 idx set
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            visited[i][j] = True
        else:
            if not visited[i][j] and matrix[i][j] == 1:
                cur_idx = bfs(i, j, prev_idx)
                prev_idx = cur_idx
                island_set.add(cur_idx)

matrix_t = [list(lst) for lst in zip(*matrix)]
graph = [[False] * (len(island_set) + 1)] + [
    [False] * (len(island_set) + 1) for _ in range(len(island_set))
]


def find_bridge(lst):
    global graph
    """
    다리, 다리 길이 찾는 함수 
    return List(tuple(섬1, 섬2, 다리길이))
    """
    island = set(lst)
    if 0 not in island:
        return
    island = list(set(lst) - set([0]))

    if len(island) < 2:
        return
    elif len(island) >= 2:
        island_idx = []
        for isl in island:
            b = False
            i = 0
            while b != True:
                try:
                    tmp_idx = lst.index(isl, i)
                    island_idx.append((tmp_idx, isl))
                    i = tmp_idx + 1
                except:
                    break
        island_idx.sort()
        sea_idx = []  # [lst.index(0, idx) for idx, _ in island_idx[:-1]]
        b = False
        for idx, _ in island_idx[:-1]:
            try:
                tmp_idx = lst.index(0, idx)
                sea_idx.append(tmp_idx)
            except:
                break
        for i in range(len(island_idx) - 1):
            (is1_idx, is1), (is2_idx, is2) = island_idx[i : i + 2]
            if is1 == is2:
                continue
            is1, is2 = sorted([is1, is2])
            for sea_start_idx in sea_idx:
                if is1_idx < sea_start_idx < is2_idx:
                    b_len = graph[is1][is2]
                    if (
                        b_len
                        and b_len > is2_idx - sea_start_idx
                        and is2_idx - sea_start_idx >= 2
                    ):
                        graph[is1][is2] = is2_idx - sea_start_idx
                    elif not b_len and is2_idx - sea_start_idx >= 2:
                        graph[is1][is2] = is2_idx - sea_start_idx


# 가로 가능한 다리 찾기
for i in range(N):
    find_bridge(matrix[i])

for i in range(M):
    find_bridge(matrix_t[i])

edges = []
for i in range(len(island_set) + 1):
    for j in range(len(island_set) + 1):
        if graph[i][j]:
            edges.append((graph[i][j], i, j))


def find_set(parent, x):
    """
    x의 루트(대표) 노드를 찾는 함수 (경로 압축 적용).
    """
    if parent[x] != x:
        parent[x] = find_set(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    """
    두 원소 x, y를 같은 집합으로 합치는 함수.
    """
    root_x = find_set(parent, x)
    root_y = find_set(parent, y)
    if root_x < root_y:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y


def kruskal_mst(num_vertices, edges):
    """
    Kruskal 알고리즘으로 MST를 찾는 함수.
    """
    # 1. 간선들을 가중치(cost) 기준으로 오름차순 정렬
    edges.sort()

    # 2. Union-Find를 위한 parent 리스트 초기화 (각자 자신이 대표)
    parent = [i for i in range(num_vertices + 1)]

    mst_cost = 0  # MST의 총 가중치
    edges_count = 0  # MST에 포함된 간선의 수
    break_point = False
    # 3. 가장 가중치가 낮은 간선부터 순회
    for cost, s, e in edges:
        # 4. 두 정점의 대표가 다른지 확인 (사이클 생성 여부 체크)
        if find_set(parent, s) != find_set(parent, e):
            # 5. 사이클이 생기지 않으면, 간선을 MST에 포함시키고
            #    두 정점을 같은 집합으로 합침 (union)
            union(parent, s, e)
            mst_cost += cost
            edges_count += 1

            # MST는 V-1개의 간선으로 이루어지므로, 다 찾았으면 종료
            if edges_count == num_vertices - 1:
                break_point = True
                break
    if break_point:
        return mst_cost
    else:
        return -1


if len(edges) < len(island_set) - 1:
    result = -1
else:
    result = kruskal_mst(len(island_set), edges)

print(f"{result}")
