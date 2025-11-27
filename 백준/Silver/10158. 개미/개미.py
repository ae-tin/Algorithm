
w, h = map(int, input().split())
p, q = map(int, input().split())

T = int(input())

p1, q1 = p+T, q+T
if p1//w % 2 == 0:
    a = p1%w
else: 
    a = w - p1%w

if q1//h % 2 == 0:
    b = q1%h
else: 
    b = h - q1%h

print(f'{a} {b}')