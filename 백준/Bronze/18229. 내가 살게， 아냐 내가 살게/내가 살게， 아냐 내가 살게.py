N, M, K = map(int, input().split())
handsup = [list(map(int, input().split())) for _ in range(N)]
result = [0]*N
for i, one_hand in enumerate(handsup):
    cum = 0
    for j, hand in enumerate(one_hand):
        cum += hand
        if cum >= K:
            result[i] = j
            break
    else:
        result[i] = M + 1
min_hand = min(result)
min_idx = result.index(min_hand)
print(f'{min_idx+1} {min_hand+1}')