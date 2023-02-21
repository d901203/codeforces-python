n, k = map(int, input().split())
s = list(input())
for _ in range(k):
    i = 1
    while i < n:
        if s[i - 1] == "B" and s[i] == "G":
            s[i - 1], s[i] = s[i], s[i - 1]
            i += 2
        else:
            i += 1
print(*s, sep="")
