N = int(input())
A = list(map(int, input().split()))

answer = []
active = True

for a in A:
    if active and a == 1:
        answer.append("o")
    else:
        answer.append("x")
        active = False

print("".join(answer))