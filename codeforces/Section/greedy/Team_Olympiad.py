n = int(input())
a = list(map(int, input().split()))

one = []
two = []
three = []

for i in range(n):
    if a[i] == 1:
        one.append(i + 1)
    elif a[i] == 2:
        two.append(i + 1)
    else:
        three.append(i + 1)

teams = min(len(one), len(two), len(three))

print(teams)

for i in range(teams):
    print(one[i], two[i], three[i])