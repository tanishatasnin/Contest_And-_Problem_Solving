t=int(input())
for _ in range(t):
    n, k=map(int,input().split())
    a=list(map(int,input().split()))
    if k==1 and a!=sorted(a):
        print("no")
    else:
        print("yes")
