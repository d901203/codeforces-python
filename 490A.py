n = int(input())
x = list(map(int, input().split()))
a = [i + 1 for i, j in enumerate(x) if j == 1]
b = [i + 1 for i, j in enumerate(x) if j == 2]
c = [i + 1 for i, j in enumerate(x) if j == 3]
if not a or not b or not c:
    print(0)
else:
    print(min(len(a), len(b), len(c)))
    for i, j, k in zip(a, b, c):
        print(i, j, k)
     