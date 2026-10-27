t=int(input())
for _ in range(t):
    a,b,c=list(map(int,input().split()))
    x,y,z=sorted([a,b,c])
    print(y)