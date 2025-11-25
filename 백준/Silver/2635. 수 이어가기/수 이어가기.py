N = int(input())

bound = [0, N]
lb, ub = bound
array = [1, 1]
n = k = 1
while True:
    if n % 2 == 1:
        ub = (array[0]/array[1])*N
        if int(ub) != ub:
            ub = int(ub)
        else: 
            ub = int(ub)
    else:
        lb = (array[0]/array[1])*N
        if int(lb) != lb:
            lb = int(lb+1)
        else:
            lb = int(lb)
    
    array.append(array[0] + array[1])
    array.pop(0)
    
    n += 1
    if abs(ub - lb) <= 1:
        k += 1
        if ub == lb:
            break
        if k > 2:
            break
        
# if N==1 : ub=lb=1
result = [N, ub]
result2 = [N, lb]
m = 1
break_point1 = False
break_point2 = False
while True:
    if not break_point1:
        result.append(result[-2] - result[-1])
        if result[-1]<0:
            answer = 1
            break_point1 = True
    
    if not break_point2:
        result2.append(result2[-2] - result2[-1])
        if result2[-1]<0:
            answer = 0
            break_point2 = True
        
    m += 1
    if break_point1 + break_point2 == 2:
        break

print(m)
if answer:
    print(' '.join(map(str,result[:-1])))
else:
    print(' '.join(map(str,result2[:-1])))