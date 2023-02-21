t = int(input())
a = [i for i in range(1, 10001) if i % 3 != 0 and i % 10 != 3]
for _ in range(t):
    n = int(input())
    print(a[n - 1])
