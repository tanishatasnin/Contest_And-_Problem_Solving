n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
if a == b:
    print("Yes")
    exit()
l = 0
while a[l] == b[l]:
    l += 1
r = n - 1
while a[r] == b[r]:
    r -= 1
case1 = a[l + 1:r + 1] == b[l:r] and a[l] == b[r]
case2 = a[l:r] == b[l + 1:r + 1] and a[r] == b[l]
print("Yes" if case1 or case2 else "No")