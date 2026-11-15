import sys

input = sys.stdin.buffer.readline

def diversity(ones, n):
    zeros = n - ones
    return 1 + ones*(ones + 1)//2 + zeros*(zeros + 1)//2

t = int(input())
answers = []
for _ in range(t):
    n, k = map(int, input().split())
    least_diverse2 = input().strip()
    ones = least_diverse2.count(b'1')
    low = max(0, ones - k)
    high = min(n, ones + k)
    answers.append(str(max(
        diversity(low, n),
        diversity(high, n)
    )))
print("\n".join(answers))