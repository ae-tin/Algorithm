def solution(files):
    tmp_sort = []
    sort_dict = dict()
    
    for f in files:
        tmp_f = f.lower()
        new_f = ""
        tmp_digit = ""
        break_point = 0
        for k in tmp_f:
            if k.isdigit():
                break_point += 1
                tmp_digit += k
            else:
                if break_point > 0:
                    break
                else:
                    new_f += k
        key = new_f + str(int(tmp_digit))
        sort_dict[key] = sort_dict.setdefault(key,0) + 1
        tmp_sort.append((new_f, int(tmp_digit), sort_dict[key], f))
    tmp_sort.sort()
    answer = []
    for _, _, _, origin in tmp_sort:
        answer.append(origin)
    
    return answer