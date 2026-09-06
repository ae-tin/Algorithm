def solution(m, n, board):
    from collections import deque
    import copy
    # 오른쪽으로 90도 회전해서 리스트로
    # 좌측 상단에서만 탐색.(우, 하, 우하대각) 그래서 2x2면 표시 (문자열 옆에 0붙이기?)
    ## 지우기
    maps_e = [list(row) for row in zip(*board[::-1])]
    maps_s = []
    answer = 0
    
    dr = [0, 1, 1] # 우 우하대각 하 만 확인
    dc = [1, 1, 0]
    q = deque([])
    # 지워지지 않으면 종료
    while maps_s != maps_e:
        # 같은 모양 표시
        maps_s = copy.deepcopy(maps_e)
        for i in range(n-1): # 행(높이)
            for j in range(m-1): # 열(폭)
                s = maps_s[i][j][0]
                if s == "x":
                    continue
                tmp_set = [(i,j)]
                for k in range(3):
                    ni, nj = i + dr[k], j + dc[k]
                    # 같은 모양이면 좌표 저장
                    if maps_s[ni][nj][0] == s:
                        tmp_set.append((ni, nj))
                        pass
                if len(tmp_set) == 4:
                    for r, c in tmp_set:
                        # 2x2 모양이면 마킹
                        maps_s[r][c] = maps_s[r][c] + "0"
        # 지우기
        maps_e = copy.deepcopy(maps_s)
        for i in range(n): # 행(높이)
            for j in range(m-1, -1, -1): # 열(폭)
                if "0" in maps_e[i][j]:
                    tmp_list = maps_e[i]
                    tmp_list.pop(j)
                    tmp_list.append("x")
                    maps_e[i] = tmp_list
                    answer += 1
    return answer