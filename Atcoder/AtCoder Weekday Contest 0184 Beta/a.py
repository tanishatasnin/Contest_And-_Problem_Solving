n,c = map(int,input().split())  
for _ in range(n):
    a , w = map(int,input().split())
    total= a*w #28
    if total>c:   
        print(total-c) 
    else: 
        print(0)
