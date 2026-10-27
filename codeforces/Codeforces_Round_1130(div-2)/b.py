import sys

def solve():
    input = sys.stdin.readline
    t = int(input())
    ans = []
    for _ in range(t):
        n = int(input())
        top = input().strip()
        bottom = input().strip()
        frogs = top.count('f') + bottom.count('f')
        ans.append(str(frogs % 2))
    print("\n".join(ans))


if __name__ == "__main__":
    solve()