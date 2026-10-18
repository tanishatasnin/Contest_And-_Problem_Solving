# The first line contains a non-empty string s — the sum Xenia needs to count. String s contains no spaces. It only contains digits and characters "+". Besides, string s is a correct sum of numbers 1, 2 and 3. String s is at most 100 characters long.

s= input()
s = s.split('+')

if len(s) == 1:
    print(s[0])
else:
    s.sort()
    print('+'.join(s)) 