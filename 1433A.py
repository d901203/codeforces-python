t = int(input())
for _ in range(t):
    s = input()
    n = int(s[-1]) - 1
    print(n * 10 + sum(range(1, len(s) + 1)))
