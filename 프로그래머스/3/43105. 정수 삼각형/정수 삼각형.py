def solution(triangle):
    dp = [[0]*i for i in range(1, len(triangle)+1)]
    dp[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        dp[i][0] = triangle[i][0] + dp[i-1][0]
        dp[i][-1] = triangle[i][-1] + dp[i-1][-1]
        
    for j in range(2, len(triangle)):
        for k in range(1, len(triangle[j])-1):
            dp[j][k] = max(dp[j-1][k-1] + triangle[j][k], dp[j-1][k] + triangle[j][k])
            
    return max(dp[-1])