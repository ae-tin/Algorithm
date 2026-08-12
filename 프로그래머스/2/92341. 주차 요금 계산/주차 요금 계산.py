def solution(fees, records):
    fix_out = 23*60 + 59
    num_record = dict()
    num_cum = dict()
    all_num = []
    for rec in records:
        # 전처리
        time, car_num, inout = rec.split(" ")
        h, m = map(int, time.split(":"))
        total_min = h*60 + m
        if not h and not m:
            total_min = 1e-3
        car_num = int(car_num)
        all_num.append(car_num)
        if num_record.get(car_num, None):
            num_cum[car_num] = num_cum.setdefault(car_num, 0) + total_min - num_record[car_num]
            del num_record[car_num]
        else:
            num_record[car_num] = total_min
    else:
        for num in all_num:
            if num_record.get(num, None):
                num_cum[num] = num_cum.setdefault(num, 0) + fix_out - num_record[num]
                del num_record[num]
    
    all_record = sorted(list(num_cum.items()))
    min_time, basic_fee, per_m, per_fee = fees
    answer = []
    for num, cum_m in all_record:
        if cum_m <= min_time:
            answer.append(basic_fee)
        else:
            if (cum_m - min_time)%per_m == 0:
                total_per_min = (cum_m - min_time)//per_m
            else:
                total_per_min = (cum_m - min_time)//per_m + 1
            answer.append(basic_fee + total_per_min * per_fee)
    
    
    return answer