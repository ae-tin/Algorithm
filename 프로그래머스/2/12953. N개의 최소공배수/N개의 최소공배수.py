def solution(arr):
    answer = 1
    while True:
        max_v = max(arr)
        prev_sum = sum(arr)
        for i in range(2, max_v + 1):
            tmp_idx = []
            for j, a in enumerate(arr):
                if a % i == 0:
                    tmp_idx.append(j)
                    
            if len(tmp_idx) >= 2:
                for idx in tmp_idx:
                    arr[idx] = int(arr[idx] / i) 
                answer *= i
                break
                    
                
        if sum(arr) == prev_sum:
            break
    for k in arr:
        answer *= k
    return answer