n, m = map(int, input().split())
a = "#" * m
b = "." * (m - 1) + "#"
f = 1
for i in range(n):
    if i & 1:
        print(b[::f])
        f = -f
    else:
        print(a)
