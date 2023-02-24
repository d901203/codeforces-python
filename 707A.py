n, m = map(int, input().split())
f = 0
for _ in range(n):
    s = input().split()
    for c in "CMY":
        if c in s:
            f = 1
            break
    if f:
        break
if f:
    print("#Color")
else:
    print("#Black&White")
