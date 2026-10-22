import bisect

N, M = map(int, input().split())
D = list(map(int, input().split()))
S = list(map(int, input().split()))

D.sort()

for com in S:
    print(bisect.bisect_right(D, com))