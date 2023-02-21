s = input()
cnt = 0
for c in s:
    if c in "47":
        cnt += 1
if all(c in "47" for c in str(cnt)):
    print("YES")
else:
    print("NO")
