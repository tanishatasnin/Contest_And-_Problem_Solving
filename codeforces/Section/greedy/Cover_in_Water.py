t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    if "..." in s:
        print(2)
    else:
        print(s.count("."))