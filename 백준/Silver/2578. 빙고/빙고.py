bingo_set = []
matrix = [list(map(int, input().split())) for _ in range(5)]
matrix_rev = [list(lst) for lst in zip(*matrix)]
x1 = []
x2 = []
for i in range(5):
    bingo_set.append(set(matrix[i]))
    bingo_set.append(set(matrix_rev[i]))
    x1.append(matrix[i][i])
    x2.append(matrix[i][4-i])
bingo_set.append(set(x1))
bingo_set.append(set(x2))
inputs = []
for _ in range(5):
    inputs.extend(list(map(int, input().split())))
k = 0
n = 0
while True : 
    for b_set in bingo_set:
        if inputs[k] in b_set:
            b_set.discard(inputs[k])
            if len(b_set) == 0:
                n += 1
    if n >= 3:
        break
    k += 1

print(f'{k+1}')