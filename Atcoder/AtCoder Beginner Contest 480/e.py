from math import factorial

N = int(input())
answer = 0


def valid(a, d, length):
    product = 1

    for i in range(length):
        product *= a + i * d

        if product > N:
            return False

    return True


length = 3

while factorial(length) <= N:
    a = 1

    while valid(a, 1, length):
        low, high = 1, N

        while low < high:
            mid = (low + high + 1) // 2

            if valid(a, mid, length):
                low = mid
            else:
                high = mid - 1

        answer += low
        a += 1

    length += 1

print(answer)