n = int(input())
result = 0
for _ in range(n):
    a, b = map(int, input().split())
    if b - a >= 2:
        result += 1
print(result)
