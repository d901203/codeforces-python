t = int(input())
for _ in range(t):
    a, b, c, n = map(int, input().split())
    x = max(a, b, c)
    t = 3 * x - (a + b + c)
    if n >= t and (n - t) % 3 == 0:
        print("YES")
    else:
        print("NO")
