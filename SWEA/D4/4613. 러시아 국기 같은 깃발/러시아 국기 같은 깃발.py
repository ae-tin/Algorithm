T = int(input())
for test_case in range(1,T+1):
    
    N, M = map(int,input().split())
    matrix = [input() for _ in range(N)]
    need_change = {
        'W':[],
        'B':[],
        'R':[]
        }
    for key in need_change.keys():
        for row in matrix:
            need_change[key].append(M - row.count(key))
    
    min_change = N * M
    
    def order_pass(order_list):
        pre = 'W'
        for a in order_list:
            if pre == 'W':
                pre = a
                continue
            elif pre == 'B':
                if a == 'W':
                    return False
                else:
                    pre = a
            elif pre == 'R':
                if a == 'W' or a == 'B':
                    return False
                else:
                    pre = a
        else:
            return True
    
    def dfs(depth, cnt, uses):
        global min_change
        if sum(cnt) > min_change:
            return
        if not order_pass(uses):
            return
        if depth == N - 2:
            if 'B' not in uses:
                return 
            if len(uses) != N - 2 :
                return
            # cnt = [need_change[key][i+1] for i, key in enumerate(uses)]
            
            min_change = min(min_change, sum(cnt))
            return
        
        #'W'
        uses.append('W')
        cnt.append(need_change['W'][depth+1])
        dfs(depth+1,cnt,uses)
        uses.pop()
        cnt.pop()
        #'B'
        uses.append('B')
        cnt.append(need_change['B'][depth+1])
        dfs(depth+1,cnt,uses)
        uses.pop()
        cnt.pop()
        #'R'
        uses.append('R')
        cnt.append(need_change['R'][depth+1])
        dfs(depth+1,cnt,uses)
        uses.pop()
        cnt.pop()
        
    dfs(0,[],[])
    
    
    min_change += need_change['W'][0] + need_change['R'][-1]
    
    
    print(f"#{test_case} {min_change}")