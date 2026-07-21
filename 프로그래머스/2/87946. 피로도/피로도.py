def solution(k, dungeons):
    answer = 0
    visited = [False] * len(dungeons)

    def dfs(tired, count):
        nonlocal answer
        answer = max(answer, count)

        for i in range(len(dungeons)):
            min_tired, cost = dungeons[i]

            if not visited[i] and tired >= min_tired:
                visited[i] = True
                dfs(tired - cost, count + 1)
                visited[i] = False

    dfs(k, 0)
    return answer