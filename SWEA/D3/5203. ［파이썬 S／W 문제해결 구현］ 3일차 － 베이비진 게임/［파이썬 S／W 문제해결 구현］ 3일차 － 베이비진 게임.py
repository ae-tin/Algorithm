def is_triplet(arr):
    a = sorted(arr)
    prev = a[0]
    cnt = 0
    for k in a:
        if prev == k: 
            cnt += 1
            if cnt == 3: return True
        else :
            prev = k
            cnt = 1
    else : return False

def is_run(arr):
    a = sorted(list(set(arr)))
    prev = a[0]
    score = 1
    for i in range(1, len(a)):
        if prev + 1 == a[i]: 
            prev = a[i]
            score += 1
            if score == 3 : return True
        else :
            prev = a[i]
            score = 1
    else : return False


T = int(input())

for test_case in range(1,T+1):
    player1, player2 = [], []
    result1, result2 = 0, 0
    for i, c in enumerate(map(int, input().split())):
        # 플레이어가 동시에 카드를 받는게 아니라 플레이어1이 4장 플레이어2가 3장을 갖고 있어도 검사가 가능하다고 가정
        if i % 2 == 0:
            player1.append(c)
            if len(player1) >= 3 :
                if is_run(player1) or is_triplet(player1):
                    print(f'#{test_case} 1')
                    break
        else : 
            player2.append(c)
            if len(player2) >= 3 :
                if is_run(player2) or is_triplet(player2):
                    print(f'#{test_case} 2')
                    break
        # 플레이어가 카드를 동시에 받는다고 가정
        # if i % 2 == 0:
        #     player1.append(c)
        # else : 
        #     player2.append(c)
        #     if len(player2) >= 3 :
        #         if is_run(player1) or is_triplet(player1): result1 = 1
        #         if is_run(player2) or is_triplet(player2): result2 = 1
        #         if result1 == 1 or result2 == 1:
        #             if result1 == 1 and result2 == 1 :  
        #                 print(f'#{test_case} 0')
        #                 break
        #             elif result1 == 1 : 
        #                 print(f'#{test_case} 1')
        #                 break
        #             elif result2 == 1 : 
        #                 print(f'#{test_case} 2')
        #                 break
    else: print(f'#{test_case} 0')