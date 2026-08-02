def solution(land):
    dp = land[0][:]

    for row in land[1:]:
        dp = [
            row[0] + max(dp[1], dp[2], dp[3]),
            row[1] + max(dp[0], dp[2], dp[3]),
            row[2] + max(dp[0], dp[1], dp[3]),
            row[3] + max(dp[0], dp[1], dp[2]),
        ]

    return max(dp)