t=int(input())
for _ in range(t):
    numbers=int(input())
    arr=list(map(int, input().split()))
    if  len(arr)==len(set(arr)):  
        print("YES")
    else:
        print("NO")
