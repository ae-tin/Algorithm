def solution(begin, target, words):
    from collections import deque

    if target not in words:
        return 0

    start = len(words)
    graph = [[] for _ in range(len(words) + 1)]

    def is_connected(word1, word2):
        return sum(a != b for a, b in zip(word1, word2)) == 1

    # begin과 한 글자 차이 나는 단어 연결
    for i, word in enumerate(words):
        if is_connected(begin, word):
            graph[start].append(i)

    # words 내부 단어끼리 양방향 연결
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_connected(words[i], words[j]):
                graph[i].append(j)
                graph[j].append(i)

    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        current, count = queue.popleft()

        for next_node in graph[current]:
            if next_node in visited:
                continue

            if words[next_node] == target:
                return count + 1

            visited.add(next_node)
            queue.append((next_node, count + 1))

    return 0