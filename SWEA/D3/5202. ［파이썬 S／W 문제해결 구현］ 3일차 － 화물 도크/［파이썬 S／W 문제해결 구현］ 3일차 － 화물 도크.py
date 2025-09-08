T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    trans = [tuple(map(int, input().split())) for _ in range(N)]
    # 빨리 끝나는 것 중 빨리 시작하는 것들로 정렬
    trans.sort(key=lambda x: (x[1], x[0]))
    # 맨 처음 건 무조건 갈 수 있으니 저장
    result = 1
    # 맨 처음 것의 출발, 도착, 다음 비교할 것 인덱스 저장
    (s, e), n_idx = trans[0], 1
    while n_idx != N:
        # 다음 끝나는 시간과 비교
        n_s, n_e = trans[n_idx]
        if e > n_s :
            n_idx += 1
            continue
        elif e <= n_s:
            s, e = n_s, n_e
            n_idx += 1
            result += 1

    print(f'#{test_case} {result}')