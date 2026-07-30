def solution(word):
    alpha = ["A","E","I","O","U"]
    answer = 0
    cnt = 0
    tmp_word = ""
    def count(alpha, tmp_word, k):
        nonlocal answer, cnt
        if k == 5:
            return 
        
        for i, a in enumerate(alpha):
            cnt += 1
            tmp_word = tmp_word + a
            if tmp_word == word:
                answer = cnt
            count(alpha, tmp_word, len(tmp_word))
            tmp_word = tmp_word[:-1]
            
    count(alpha, tmp_word, 0)
    return answer