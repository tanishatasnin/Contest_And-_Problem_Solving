string_1=input().lower()
string_2=input().lower()

string_1=string_1[::-1]

if string_1==string_2:
    print("YES")
else:
    print("NO")