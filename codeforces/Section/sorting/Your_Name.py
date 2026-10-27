t=int(input())
for _ in range(t):
    n = int(input())
    s, t = input().split()

    print("YES" if sorted(s) == sorted(t) else "NO")