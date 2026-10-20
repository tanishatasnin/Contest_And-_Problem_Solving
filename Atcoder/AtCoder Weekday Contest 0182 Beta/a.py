# Takahashi conducted 
# N experiments using a balance scale. In the 
# i-th experiment, he placed a weight of 
# A 
# i
# ​
#   grams on the left pan and a weight of 
# B 
# i
# ​
#   grams on the right pan.

# For each experiment, print Left if the left pan goes down, Right if the right pan goes down, and Balanced if the scale balances. The heavier pan goes down.

n=int(input())
for _ in range(n):
    a,b= list(map(int,input().split()))
    if a>b:
        print("left")
    elif a<b:
        print("right")
    else:
        print("Balanced")

