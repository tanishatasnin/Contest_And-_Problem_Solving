# Takahashi's company has H employees, and attendance 
# records have been kept for W days. The records are given 
# as H strings S 1 ​ ,S 2 ​ ,…,S H ​ . If the j-th character of S i ​ is o, 
# the i-th employee attended on day j; if it is x, they did not. 
# Find the number of employees with "perfect attendance,"
#  meaning they attended on all W days. 

h, w=map(int,input().split())
employ_records = list(input() for _ in range(h))
count = 0
for i in range(h):
    if employ_records[i].count("o") == w:
        count += 1
print(count)