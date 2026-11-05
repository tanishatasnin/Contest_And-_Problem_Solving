
n=int(input())
for _ in range(n):
    a,b= list(map(int,input().split()))
    if a>b:
        print("left")
    elif a<b:
        print("right")
    else:
        print("Balanced")

