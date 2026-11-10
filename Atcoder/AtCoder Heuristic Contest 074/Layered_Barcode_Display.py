import sys


def main() -> None:
    input = sys.stdin.readline

    first = input().split()
    if not first:
        return
    n, k, p, r = map(int, first)
    barcodes = [input().strip() for _ in range(p)]
    if k < 2 * n:
        raise ValueError("This construction requires K >= 2*N")
    designs = []
    for j in range(n):
        white = ["."] * n
        black = ["."] * n
        white[j] = "0"
        black[j] = "1"
        designs.append("".join(white))
        designs.append("".join(black))
    designs.extend(["." * n] * (k - 2 * n))

    sys.stdout.write("\n".join(designs) + "\n")
    sys.stdout.flush()

    order = list(range(k))
    current = ["0"] * n

    for _ in range(r):
        line = input()
        if not line:
            return
        query = int(line)
        if query < 0:
            return
        target = barcodes[query]
        operations = []

        for j, wanted in enumerate(target):
            if current[j] == wanted:
                continue

            white_id = 2 * j
            black_id = white_id + 1
            position_white = order.index(white_id)
            position_black = order.index(black_id)
            
            moving = white_id if position_white < position_black else black_id
            other = black_id if moving == white_id else white_id
            order.remove(moving)
            insertion = order.index(other) + 1
            order.insert(insertion, moving)

            operations.append((moving, insertion))
            current[j] = wanted

        output = [str(len(operations))]
        output.extend(f"{sheet} {d}" for sheet, d in operations)
        sys.stdout.write("\n".join(output) + "\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main()