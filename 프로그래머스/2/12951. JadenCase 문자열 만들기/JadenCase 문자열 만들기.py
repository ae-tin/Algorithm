# def solution(s):
#     s = s.lower()
#     jadencase = []
#     for ss in s.split(" "):
#         if ss != " " and not ss[0].isdigit():
#             jadencase.append(ss[0].upper() + ss[1:].lower())
#         else:
#             jadencase.append(ss.lower())
#     # strings = list(map(lambda string: string[0].upper() + string[1:].lower() if string != " " and not string[0].isdigit() else string.lower(), s.split(" ")))
#     # jadencase = [ string[0].upper() + string[1:] if string != " " and not string[0].isdigit() else string for string in strings]    
#     return " ".join(jadencase)


# def solution(s):
#     answer = ''
#     words = s.split(" ")    
#     for i, word in enumerate(words):
#         if word and not word.isdigit(): 
#             f_letter = word[0].upper()
#             rest_word = word[1:].lower()
#             words[i] = f_letter + rest_word
#     return ' '.join(words)


def solution(s):
    words = s.split(" ")
    answer = [word[0].upper()+word[1:].lower() if word else "" for word in words]
    return " ".join(answer)