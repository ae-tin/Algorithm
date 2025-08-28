N = int(input())
rows = [0]*(N)  # 0..N-1

for i in range(N):
    bits = 0
    for j, v in enumerate(map(int, input().split())):
        if v:  # v == 1이면 i의 이웃 j를 비트로 켭니다
            bits |= 1 << j
    rows[i] = bits

S = 0
for u in range(N):
    ru = rows[u]
    for v in range(u+1, N):
        c = (ru & rows[v]).bit_count()  # 공통 이웃 수
        if c >= 2:
            S += c*(c-1)//2             # C(c,2)

answer = 4 * S  # 순서 구분한 4-cycle 개수
print(answer)