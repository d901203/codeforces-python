n = int(input())
result = 0
for _ in range(n):
    s = input()
    result = result + 1 if "+" in s else result - 1
print(result)
