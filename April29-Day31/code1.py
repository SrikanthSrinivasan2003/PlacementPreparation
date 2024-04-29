q = int(input())
x = 0
while q > 0:
    z = q % 10
    if z % 2 == 0:
        x += z
    q //= 10
print(x)
