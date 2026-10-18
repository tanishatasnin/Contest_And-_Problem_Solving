n, m = map(int, input().split())

candidates = [input().strip() for _ in range(n)]
ballots = [input().strip() for _ in range(m)]

votes = [0] * n

for ballot in ballots:
    if ballot in candidates:
        votes[candidates.index(ballot)] += 1
        continue

    possible = []

    for i, candidate in enumerate(candidates):
        if len(candidate) != len(ballot):
            continue

        differences = sum(
            a != b for a, b in zip(candidate, ballot)
        )

        if differences == 1:
            possible.append(i)

    if len(possible) == 1:
        votes[possible[0]] += 1

for vote in votes:
    print(vote)