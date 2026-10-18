t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    compressed_length = 1

    for i in range(1, n):
        if s[i] != s[i - 1]:
            compressed_length += 1

    answer = compressed_length
    for i in range(1, n - 1):
        old_connections = (
            (s[i - 1] != s[i]) +
            (s[i] != s[i + 1])
        )

        new_connection = s[i - 1] != s[i + 1]

        candidate = compressed_length - old_connections + new_connection

        answer = min(answer, candidate)

    print(answer)