n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
if len(set(a[1:] + b[1:])) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
