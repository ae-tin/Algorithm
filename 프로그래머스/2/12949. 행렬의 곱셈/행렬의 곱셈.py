def solution(arr1, arr2):
    m, k, n = len(arr1), len(arr1[0]), len(arr2[0])
    answer = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for h in range(len(arr1[i])):
                answer[i][j] += arr1[i][h] * arr2[h][j]
    
    return answer