N = int(input())

index = {
    (1,3):
        {3:1,1:0},
    (2,4):
        {4:1,2:0},
    (2,3):
        {2:1,3:0},
    (1,4):
        {1:1,4:0},    
    }
pair = []
sums = [[] for _ in range(5)]
large = 1
small = 1
inputs = [tuple(map(int, input().split())) for _ in range(6)]
for d, length in inputs:
    sums[d].append(length)
    if len(sums[d]) == 2:
        large *= sum(sums[d])
        pair.append(d)
pair.sort()
pair = tuple(pair)

while True:
    if len(sums[inputs[0][0]]) == 2:
        inputs.append(inputs.pop(0))
    elif len(sums[inputs[0][0]]) == 1:
        break
    
sums2 = [[] for _ in range(5)]
for d, length in inputs:
    sums2[d].append(length)
    

idx = index[tuple(pair)]
small *= sums2[pair[0]][idx[pair[0]]] * sums2[pair[1]][idx[pair[1]]]    

result = (large - small) * N
print(f'{result}')