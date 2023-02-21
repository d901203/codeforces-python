t = int(input())
for _ in range(t):
    n = int(input())
    n //= 2
    if n % 2:
        print("NO")
    else:
        print("YES")
        a = [2 * i for i in range(1, n + 1)]
        b = [2 * i - 1 for i in range(1, n)]
        c = sum(a) - sum(b)
        print(*a, *b, c)
