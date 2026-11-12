t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    manual = 0
    current = 'R'
    for ch in s:
        if current != ch:
            manual += 1
            current = ch
        current = 'B' if current == 'R' else 'R'
    print(manual)