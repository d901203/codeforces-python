n = int(input())
while True:
    n += 1
    a = str(n)
    if len(a) == len(set(a)):
        print(a)
        exit()
