t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    result = 0
    if a < b:
        if (b - a) % 2:
            result = 1
        else:
            result = 2
    elif a > b:
        if (a - b) % 2:
            result = 2
        else:
            result = 1
    print(result)
