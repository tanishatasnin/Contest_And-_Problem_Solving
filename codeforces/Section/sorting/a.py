import sys
from collections import Counter

data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
pos = 1
ans = []

for _ in range(t):
    n = data[pos]
    pos += 1

    a = data[pos:pos + n]
    pos += n

    count = Counter(a)

    result = -1
    for x in a:
        if count[x] >= 3:
            result = x
            break

    ans.append(str(result))

print("\n".join(ans))