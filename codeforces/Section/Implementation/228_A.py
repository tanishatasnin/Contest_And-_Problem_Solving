s1,s2,s3,s4=map(int,input().split())
if s1==s2==s3==s4:
    print(3)
elif s1==s2==s3 or s1==s2==s4 or s1==s3==s4 or s2==s3==s4:
    print(2)
elif s1==s2 or s1==s3 or s1==s4 or s2==s3 or s2==s4 or s3==s4:
    print(1)
else:
    print(0)


