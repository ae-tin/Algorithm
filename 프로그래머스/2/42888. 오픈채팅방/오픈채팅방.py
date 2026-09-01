def solution(record):
    enter_leave = []
    naming = {}
    # 이름 관리 -> uid의 이름 관리 -> 딕셔너리?
    # enter_leave -> 입출입 관리
    
    for r in record:
        sp = r.split(" ")
        if sp[0] == "Leave":
            enter_leave.append(("Leave",sp[1]))
        else:
            EL, uid, name = sp[0], sp[1], sp[2]
            if EL == "Enter":
                naming[uid] = name
                enter_leave.append(("Enter",uid))
            else:
                naming[uid] = name
    
    answer = []
    for EL, uid in enter_leave:
        tmp_str = ""
        if EL == "Enter":
            tmp_str += naming[uid] + "님이 들어왔습니다."
        else:
            tmp_str += naming[uid] + "님이 나갔습니다."
        answer.append(tmp_str)
        
    return answer