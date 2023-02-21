a, b = map(int, input().split())
result = 0
while a <= b:
    result += 1
    a *= 3
    b *= 2
print(result)
