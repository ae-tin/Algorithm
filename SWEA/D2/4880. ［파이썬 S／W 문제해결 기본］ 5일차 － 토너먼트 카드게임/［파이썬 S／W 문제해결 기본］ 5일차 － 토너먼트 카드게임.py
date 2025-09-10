T = int(input())

def merge(left, right):
    if left and right :
        if abs(left[0][0] - right[0][0]) == 1:
            return [sorted(left + right, key = lambda x: x[0])[1]]
        elif abs(left[0][0] - right[0][0]) == 0:
            return [sorted(left + right, key = lambda x: x[1])[0]]
        else :
            return [sorted(left + right, key = lambda x: x[0])[0]]

def divide(lst): # 재귀적으로 나누고 조건을 만족할 때 규칙에 따라 합친다
    mid = (len(lst)+1)//2
    if len(lst) == 1: # lst가 하나만 남을때
        return lst
    elif len(lst) == 2: # lst의 원소가 두개일 때 merge
        left = lst[:mid]
        right = lst[mid:]
        return merge(left,right)
    else : # lst의 원소가 두개 이상일 때 나누고 재귀
        left = lst[:mid]
        right = lst[mid:]
        return merge(divide(left), divide(right))

for test_case in range(1,T+1):
    N = int(input())
    # 카드의 숫자랑 카드 번호를 함께 저장
    cards = [ (c, i+1) for i, c in enumerate(map(int, input().split()))]
    print(f'#{test_case} {divide(cards)[0][1]}')