n = int(input())
s = input()

answer = 0

for i in range(n):
    left = max(0, i - 1)
    right = min(n, i + 2)

    if 'G' not in s[left:right]:
        answer += 1

print(answer)