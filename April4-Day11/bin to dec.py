n = int(input())
b = bin(n)
print(b[2:])

n = int(input())
b = ""
while n>0:
    b+=str(n%2)
    n//=2
print(b[::-1])
