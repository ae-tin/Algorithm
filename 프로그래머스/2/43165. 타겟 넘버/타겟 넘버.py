def solution(numbers, target):
    n = len(numbers)
    answer = 0
    def dfs(sum_v, k):
        nonlocal answer
        if k == n:
            if sum_v == target:
                answer += 1
            return
        
        dfs(sum_v + numbers[k], k+1)
        
        dfs(sum_v - numbers[k], k+1)
        
        
    dfs(0,0)
            
    
    
    return answer