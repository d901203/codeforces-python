t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    a.sort()
    for i in range(1, n):
        if a[i] - a[i - 1] > 1:
            cnt += 1
        if cnt:
            break
    if cnt:
        print("NO")
    else:
        print("YES")
