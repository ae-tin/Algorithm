# def find_pair(s):
#     # pair를 찾고 pair를 없앤 후 반환하는 함수
#     init = s[0]
#     after = init
#     for i, ss in enumerate(s[1:]):
#         if ss != init:
#             after += ss
#             init = ss
#         else:
#             return True, after[:-1] + s[1:][i+1:]
#     else:
#         return False, after
    
# def solution(s):
#     disc = True
#     answer = 0
#     while disc:
#         disc, s = find_pair(s)
#         if len(s) == 0:
#             answer = 1
#             break

#     return answer


# def solution(s):
    # 각 원소가 몇개 있는지 보고, 어디있는지 찾아서 연속된 걸 지워나간다
    # answer = 0
    # dicts = {i:0 for i in set(s)}
    # for i in dicts.keys():
    #     i_cnt = s.count(i)
    #     dicts[i] = i_cnt
    #     # 원소가 홀수 개인 게 하나라도 있으면 소거를 못함
    #     if i_cnt % 2 == 1:
    #         return answer
    #     # 원소가 짝수개면 위치 찾고 소거
    #     else:
    #         first = s.index(i)
    #         second = s[first+1:].index(i) + first + 1
    #         if second != first + 1:
    #             continue
    #         else:
    #             s = s[:first] + s[second+1:]
    #             dicts[i] = s.count(i)
            
        
# def solution(s):
#     while True:
#         # print(s)
#         sets = set(s)
#         for i in sets:
#             i_cnt = s.count(i)
#             if i_cnt % 2 ==1:
#                 return 0
#             else:
#                 i_range = i_cnt//2
#                 for i
#                 first = s.index(i)
#                 second = s[first+1:].index(i)
#                 # print(i, s, first, s[first+1:], second)
#                 if second == 0:
#                     s = s[:first] + s[first+2:]
#                     break
                
#         else:
#             break
            
#     if len(s) == 0:
#         return 1
#     else:
#         return 0

# def solution(s):
#     i = 0
#     while True:
#         # print(i)  # 제출할 때는 제거하는 게 좋음

#         if i >= len(s) - 1:
#             break
            
#         if s[i] != s[i+1]:
#             i += 1
#             continue
#         else:
#             s = s[:i] + s[i+2:]
#             i = 0
            
#     if len(s) == 0:
#         return 1
#     else:
#         return 0

def solution(s):
    stack = []

    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    return 1 if not stack else 0