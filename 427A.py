n = int(input())
a = list(map(int, input().split()))
result = 0
cur = 0
for x in a:
    if x == -1:
        if cur - 1 < 0:
            result += 1
        else:
            cur -= 1
    else:
        cur += x
print(result)
