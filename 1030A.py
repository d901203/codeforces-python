n = int(input())
a = list(map(int, input().split()))
if any(x for x in a):
    print("HARD")
else:
    print("EASY")
