import sys

input = sys.stdin.readline

MOD = 998244353

S = input().strip()
X = input().strip()
Y = input().strip()

# State IDs
START = 0
BX = 1          
BY = 2          

state_id = {}
states = [START, BX, BY]

def get_state(t, pos):
    key = (t, pos)
    if key not in state_id:
        state_id[key] = len(states)
        states.append(key)
    return state_id[key]

for t, word in enumerate((X, Y)):
    for i in range(len(word)):
        get_state(t, i)

eps = [[] for _ in states]
go = [[-1, -1] for _ in states]

eps[START] = [get_state(0, 0), get_state(1, 0)]
eps[BX] = [get_state(0, 0), get_state(1, 0)]
eps[BY] = [get_state(0, 0)]

for t, word in enumerate((X, Y)):
    for i, ch in enumerate(word):
        u = get_state(t, i)

        for bit in (0, 1):
            if ch == '?' or ch == str(bit):
                if i + 1 == len(word):
                    go[u][bit] = BX if t == 0 else BY
                else:
                    go[u][bit] = get_state(t, i + 1)


def closure(current):
    current = set(current)
    stack = list(current)

    while stack:
        u = stack.pop()
        for v in eps[u]:
            if v not in current:
                current.add(v)
                stack.append(v)

    return frozenset(current)


def move(current, bit):
    nxt = set()

    for u in current:
        v = go[u][bit]
        if v != -1:
            nxt.add(v)

    if not nxt:
        return frozenset()

    return closure(nxt)


start = closure([START])
dp = {start: 1}

for ch in S:
    ndp = {}

    allowed = (0, 1) if ch == '?' else (int(ch),)

    for state, ways in dp.items():
        for bit in allowed:
            nxt = move(state, bit)

            if nxt:
                ndp[nxt] = (ndp.get(nxt, 0) + ways) % MOD

    dp = ndp

answer = 0

for state, ways in dp.items():
    if BX in state or BY in state:
        answer = (answer + ways) % MOD

print(answer)