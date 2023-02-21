t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    long, short = max(a, b), min(a, b)
    if short * 2 > long:
        long = short * 2
    print(long * long)
