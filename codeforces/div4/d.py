import sys

data = sys.stdin.buffer.read().split()
t = int(data[0])
p = 1

for _ in range(t):
    n = int(data[p])
    s = data[p + 1].decode()
    p += 2

    ans = 0

    for i in range(n // 2):
        ans = max(ans, abs(ord(s[i]) - ord(s[n - 1 - i])))

    print(ans)