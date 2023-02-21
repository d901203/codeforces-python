t = int(input())
for _ in range(t):
    s = input()
    result = []
    for i, x in enumerate(s):
        if int(x):
            result.append(x + "0" * (len(s) - 1 - i))
    print(len(result))
    print(*result)
