N = int(input())
S = input()

answer = sum(1 for i in range(N - 1) 
if S[i] == "C" and S[i + 1] == "A")

print(answer)