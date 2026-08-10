def solution(msg):
    alpha_dict = {
        chr(n): i + 1
        for i, n in enumerate(range(ord("A"), ord("A") + 26))
    }

    answer = []

    start = 0
    end = 1

    while start < len(msg):

        # 현재 문자열이 사전에 있으면 계속 확장
        while end <= len(msg) and msg[start:end] in alpha_dict:
            end += 1

        # 끝까지 전부 사전에 있는 경우
        if end > len(msg):
            answer.append(alpha_dict[msg[start:len(msg)]])
            break

        # msg[start:end]는 사전에 없음
        # 직전 문자열은 msg[start:end-1]
        prev_s = msg[start:end - 1]
        new_s = msg[start:end]

        answer.append(alpha_dict[prev_s])

        # 새로운 문자열 등록
        alpha_dict[new_s] = len(alpha_dict) + 1

        # 현재 새 문자부터 다시 시작
        start = end - 1
        end = start + 1

    return answer