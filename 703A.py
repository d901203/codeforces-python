n = int(input())
x = y = 0
for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        x += 1
    elif a < b:
        y += 1
if x > y:
    print("Mishka")
elif x < y:
    print("Chris")
else:
    print("Friendship is magic!^^")
