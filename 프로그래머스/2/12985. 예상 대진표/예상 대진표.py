def solution(n,a,b):
    answer = 1
    while True:
        print(a, b)
        # 현재 반복이 토너먼트 라운드라고 가정
        # 몫이 다음 라운드 번호가 됨
        a, k = divmod(a-1, 2)
        b, r = divmod(b-1, 2)
        # 보정
        a += 1
        b += 1
        # 몫이 같으면 맞붙게 된다
        if a == b:
            return answer
        
        # 몫이 다르면 다음 라운드 진행
        answer += 1
        

    return answer