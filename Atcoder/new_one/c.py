
t=int(input())
accounts = {}
for _ in range(t):
    s = input()
    if s in accounts:
        print(accounts[s])
    else:
        new_id = len(accounts) + 1
        accounts[s] = new_id
        print(new_id)