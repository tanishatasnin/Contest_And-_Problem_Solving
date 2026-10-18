
n,k=map(int,input().split())
students=list(map(int,input().split()))
teams= 0 

for i in range(n):
    if 5-students[i]>=k:
        teams+=1
print(teams//3)
        