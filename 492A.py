n = int(input())
result = 0
level = 1
while n >= level:
    n -= level
    result += 1
    level += result + 1
print(result)
