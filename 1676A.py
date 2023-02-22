t = int(input())
for _ in range(t):
    s = input()
    a = sum(int(x) for x in s[:3])
    b = sum(int(x) for x in s[-3:])
    if a == b:
        print("YES")
    else:
        print("NO")
