import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    if n <= 3:
        print(-1)
        continue
    p = [0] * n
    odd_pos = list(range(0, n, 2))  
    even_pos = list(range(1, n, 2))  

    if n % 2 == 0:
        odd_values = [4, 2] + list(range(6, n + 1, 2))
        even_values = [3, 1] + list(range(5, n, 2))
    else:
        odd_values = [4, 3, 2] + list(range(6, n, 2))
        even_values = [5, 1] + list(range(7, n + 1, 2))

    for pos, value in zip(odd_pos, odd_values):
        p[pos] = value
    for pos, value in zip(even_pos, even_values):
        p[pos] = value

    print(*p)