n = int(input())
result = 0
for i in range(1, n + 1):
    leader = i
    member = n - i
    if member < leader:
        print(result)
        break
    if member % leader == 0:
        result += 1
