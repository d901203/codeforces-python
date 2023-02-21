k, r = map(int, input().split())
result = 1
while k * result % 10 and (k * result - r) % 10:
    result += 1
print(result)
