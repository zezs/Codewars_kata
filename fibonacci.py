[a, b, n] = [0, 1, int(input("enter no"))]
for i in range(n):
    print(a)
    [a, b] = [b, a+b]