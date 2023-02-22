t = int(input())
for _ in range(t):
    a = sorted(list(map(int, input().split())))
    if a[0] + a[1] == a[-1]:
        print("YES")
    else:
        print("NO")
