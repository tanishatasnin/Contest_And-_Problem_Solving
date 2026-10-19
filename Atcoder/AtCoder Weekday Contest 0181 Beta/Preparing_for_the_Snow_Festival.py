# In Takahashi's town, a snow festival will be held in 
# D days. The snow festival requires at least 
# C centimeters of snow to be accumulated.

# As of this morning, 
# A centimeters of snow has accumulated. According to the weather forecast, exactly 
# B centimeters of snow will fall and accumulate every night from now on, and none of it will melt.

# If there is at least 
# C centimeters of snow accumulated on the morning 
# D days from now, print Yes; otherwise, print No.

a,b,c,d=map(int,input().split())
if a+b*d>=c:
    print("Yes")
else:
    print("No") 