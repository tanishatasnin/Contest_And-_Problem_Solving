a,b,c=map(int,input().split()) 
if a>=c and b>=c: 
    count=(a//c)*(b//c)
    print(count)
else:
    print(0)
