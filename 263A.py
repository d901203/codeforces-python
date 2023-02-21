for i in range(5):
    a = map(int, input().split())
    for j, x in enumerate(a):
        if x == 1:
            print(abs(i - 2) + abs(j - 2))
            exit()
