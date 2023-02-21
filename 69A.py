n = int(input())
x = y = z = 0
for _ in range(n):
    xx, yy, zz = map(int, input().split())
    x += xx
    y += yy
    z += zz
if x == y == z == 0:
    print("YES")
else:
    print("NO")
