n = int(input())
s = input()
result = 0
for i in range(1, n):
    if s[i] == s[i - 1]:
        result += 1
print(result)
