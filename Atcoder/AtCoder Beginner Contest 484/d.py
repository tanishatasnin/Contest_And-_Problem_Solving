n = int(input())
a = list(map(int, input().split()))

count = [0] * (n + 1)
answer = 1  

for i in range(n):
    if i == 0 or a[i] != a[i - 1]:
        answer += i - count[a[i]]
    count[a[i]] += 1
print(answer)