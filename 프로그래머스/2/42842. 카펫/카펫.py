def solution(brown, yellow):
    answer = []
    b = (brown-4)//2
    for i in range(1, b//2 + 1):
        if i*(b-i) == yellow:
            return [max([i+2,(b-i)+2]),min([i+2,(b-i)+2])]