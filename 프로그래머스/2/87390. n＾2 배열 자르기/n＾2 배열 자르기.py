# def solution(n, left, right):
#     array = []
#     cnt = 0
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if left <= cnt <= right:
#                 array.append(max(i,j))
#             else:
#                 cnt+=1
#                 continue
#             cnt += 1
#     return array


# def solution(n, left, right):
#     answer = []
#     i1, j1 = divmod(left, n)
#     i2, j2 = divmod(right, n)
    
    
#     for i in range(i1, i2 + 1):
#         for j in range(j1, j2 + 1):
#             print(i*n+j)
#             answer.append(max(i,j))
    
#     return answer

def solution(n, left, right):
    answer = []

    for idx in range(left, right + 1):
        row = idx // n
        col = idx % n
        answer.append(max(row, col) + 1)

    return answer
    