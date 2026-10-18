# The first input line contains a single integer n (1 ≤ n ≤ 1000) — the number of problems in the contest. Then n lines contain three integers each, each integer is either 0 or 1. If the first number in the line equals 1, then Petya is sure about the problem's solution, otherwise he isn't sure. The second number shows Vasya's view on the solution, the third number shows Tonya's view. The numbers on the lines are separated by spaces.

n= int(input())
count=0
for i in range(n):
    a,b,c=map(int,input().split())
    if a+b+c>=2:
        count+=1
print(count)

