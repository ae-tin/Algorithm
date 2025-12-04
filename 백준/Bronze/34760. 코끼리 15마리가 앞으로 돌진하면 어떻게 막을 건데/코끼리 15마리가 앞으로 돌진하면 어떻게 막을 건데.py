elephants = list(map(int, input().split()))
sort_elephants = sorted(elephants)
max_nose = max(elephants)

if max_nose == elephants[-1]:
    if max_nose == sort_elephants[-2]:
        result = max_nose + 1
    else: 
        result = max_nose
else:
    result = max_nose + 1

print(result)