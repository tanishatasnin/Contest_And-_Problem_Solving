t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    if a >= b:
        print( a + c - b )
    else:
        print( max(b - a, abs(a + c - b) ) )