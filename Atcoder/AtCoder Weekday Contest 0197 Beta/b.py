n , k =map(int,input().split())
A=list(map(int,input().split()))
ans=-1

for i in range(n):
    if A[i] >= k :
        ans=i+1
print(ans)

