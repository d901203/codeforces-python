n, k = map(int, input().split())
left = 60 * 4 - k
result = 0
for i in range(1, n + 1):
    if left - i * 5 < 0:
        break
    left -= i * 5
    result += 1
print(result)
