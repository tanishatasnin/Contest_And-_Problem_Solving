import sys

MOD = 998244353
G = 3

def ntt(a, invert):
    n = len(a)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            a[i], a[j] = a[j], a[i]

    length = 2
    while length <= n:
        wlen = pow(G, (MOD - 1) // length, MOD)
        if invert:
            wlen = pow(wlen, MOD - 2, MOD)
        half = length >> 1
        for start in range(0, n, length):
            w = 1
            for i in range(start, start + half):
                u = a[i]
                v = a[i + half] * w % MOD
                a[i] = (u + v) % MOD
                a[i + half] = (u - v) % MOD
                w = w * wlen % MOD
        length <<= 1
    if invert:
        inv_n = pow(n, MOD - 2, MOD)
        for i in range(n):
            a[i] = a[i] * inv_n % MOD


def convolution(a, b, limit):
    need = len(a) + len(b) - 1
    size = 1
    while size < need:
        size <<= 1
    fa = a + [0] * (size - len(a))
    fb = b + [0] * (size - len(b))
    ntt(fa, False)
    ntt(fb, False)

    for i in range(size):
        fa[i] = fa[i] * fb[i] % MOD
    ntt(fa, True)
    return fa[:limit]


def ask(x):
    print("?", x, flush=True)
    response = sys.stdin.readline().strip()
    if response == "-1" or response == "":
        sys.exit(0)
    return response == "Yes"

def solve_case(n):
    present = [False] * n
    for x in range(1, n):
        present[x] = ask(x)

    elements = [x for x in range(1, n) if present[x]]
    for x in elements:
        y = n - x
        if x < y < n and present[y]:
            print("!", 2, flush=True)
            return

    poly = [0] * n
    for x in elements:
        poly[x] = 1
    pair_count = convolution(poly, poly, n)
    for z in elements:
        target = n - z
        required = 2
        if target % 2 == 0 and present[target // 2]:
            required += 1
        if pair_count[target] >= required:
            print("!", 3, flush=True)
            return

    print("!", -1, flush=True)


def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        solve_case(n)


if __name__ == "__main__":
    main()