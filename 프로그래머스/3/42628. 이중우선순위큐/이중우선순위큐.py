def solution(operations):
    from collections import deque
    q = deque([])
    
    for ops in operations:
        o, d = ops.split()
        d = int(d)
        if o == "I":
            q.append(d)
        elif o == "D" and d == -1 and q:
            q = deque(sorted(q))
            q.popleft()
        elif o == "D" and d == 1 and q:
            q = deque(sorted(q))
            q.pop()
        else:
            pass
        
    else:
        if not q:
            return [0,0]
        else:
            q = deque(sorted(q))
            if len(q) >= 2:
                return [q[-1], q[0]]
            else:
                return [q[0], q[0]]