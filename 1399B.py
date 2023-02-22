t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_m = min(a)
    b_m = min(b)
    a = [x - a_m for x in a]
    b = [x - b_m for x in b]
    result = 0
    for x, y in zip(a, b):
        result += x + y - min(x, y)
    print(result)
