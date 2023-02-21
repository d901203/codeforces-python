k, n, w = map(int, input().split())
s = (1 + w) * w // 2 * k
if s > n:
    print(s - n)
else:
    print(0)
