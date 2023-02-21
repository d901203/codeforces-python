n = int(input())
result = ""
for i in range(n):
    if i & 1:
        result += "I love"
    else:
        result += "I hate"
    if i != n - 1:
        result += " that "
print(result + " it")
