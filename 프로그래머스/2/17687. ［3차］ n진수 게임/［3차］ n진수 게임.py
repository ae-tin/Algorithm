def trans(u, w):
    # u을 w진수로
    over10 = {
        10 : 'A',
        11 : 'B',
        12 : 'C',
        13 : 'D',
        14 : 'E',
        15 : 'F',
    }
    trans_w = ''
    if u == 0:
        return ['0']
    while u > 0:
        u, r = divmod(u, w)
        trans_w += over10[r] if r >= 10 else str(r)
    
    return list(trans_w[::-1])
        

def solution(n, t, m, p):
    cnt, cnt2 = 0, 0
    answer = ''
    all_answer = []
    
    while len(answer) < t:
        all_answer.extend(trans(cnt,n))
        cnt += 1
        while len(all_answer) > cnt2*m + p :
            answer += all_answer[cnt2*m + p-1]
            cnt2 += 1
            
    return answer[:t]