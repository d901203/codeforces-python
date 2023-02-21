from collections import Counter

a = Counter(input()) + Counter(input())
b = Counter(input())
if a == b:
    print("YES")
else:
    print("NO")
