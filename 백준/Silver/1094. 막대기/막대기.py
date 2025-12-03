T = int(input())
n = 0
k = 6
while T != 0:
    if T >= 2**k:
        T -= 2**k
        n += 1
        k -= 1
    else:
        if k < 0 :
            break
        k -= 1
        

print(f'{n}')