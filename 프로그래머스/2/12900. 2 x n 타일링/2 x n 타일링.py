def solution(n):
    MOD = 1_000_000_007

    if n == 1:
        return 1

    prev2 = 1  # dp[1]
    prev1 = 2  # dp[2]

    for i in range(3, n + 1):
        current = (prev1 + prev2) % MOD
        prev2 = prev1
        prev1 = current

    return prev1