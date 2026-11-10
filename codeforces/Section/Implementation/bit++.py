
n=int(input())
x=0
for i in range(n):
    s=input()
    if s[0]==s[1]=="+" or s[1]==s[2]=="+":
        x+=1
    if s[0]==s[1]=="-" or s[1]==s[2]=="-":
        x-=1
print(x)