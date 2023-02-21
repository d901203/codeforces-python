a = int(input())
s = 5
result = 0
while a and s:
    result += a // s
    a %= s
    s -= 1
print(result)
