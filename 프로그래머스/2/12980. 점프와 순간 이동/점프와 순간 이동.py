def solution(n):
    ans = 0
    while n != 0:
        n, r = divmod(n, 2)
        ans += r

    return ans