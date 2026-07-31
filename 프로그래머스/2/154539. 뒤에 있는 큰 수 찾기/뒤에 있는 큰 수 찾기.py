def solution(numbers):
    answer = [-1]*len(numbers)
    tmp_stack = []
    for i, n in enumerate(numbers):
        while tmp_stack and numbers[tmp_stack[-1]] < n:
            tmp_idx = tmp_stack.pop()
            answer[tmp_idx] = n
        tmp_stack.append(i)
    return answer