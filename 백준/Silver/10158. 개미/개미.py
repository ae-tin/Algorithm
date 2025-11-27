w, h = map(int, input().split())
p, q = map(int, input().split())
T = int(input())

a = ((-1)**(((p+T)//w)%2))*((p+T)%w) + w*(((p+T)//w)%2)
b = ((-1)**(((q+T)//h)%2))*((q+T)%h) + h*(((q+T)//h)%2)

print(f'{a} {b}')