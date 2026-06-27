def solution(n, words):
    answer = []
    word_dict = {}
    last = words[0][0]
    for i, word in enumerate(words, 1):
        a, r = divmod(i, n)
            
        if word_dict.setdefault(word, 0) == 0 and last == word[0]:
            word_dict[word] += 1
            last = word[-1]
        else:
            return [r, a + 1] if r != 0 else [n, a]
        
    return [0,0]