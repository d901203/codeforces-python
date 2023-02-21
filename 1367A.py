t = int(input())
for _ in range(t):
    s = input()
    result = ""
    for i in range(0, len(s), 2):
        result += s[i]
    result += s[-1]
    print(result)
