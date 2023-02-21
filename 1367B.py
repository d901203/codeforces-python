t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    x = y = 0
    for i, c in enumerate(a):
        if i % 2 and c % 2 == 0:
            x += 1
        elif i % 2 == 0 and c % 2:
            y += 1
    if x != y:
        print(-1)
    else:
        print(x)
