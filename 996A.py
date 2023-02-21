n = int(input())
a = [100, 20, 10, 5, 1]
result = 0
for x in a:
    if not n:
        break
    result += n // x
    n %= x
print(result)
