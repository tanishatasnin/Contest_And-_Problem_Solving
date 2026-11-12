t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())

    if b == a + 1 and c == b + 1:
        print("YES")
    else:
        print("NO")