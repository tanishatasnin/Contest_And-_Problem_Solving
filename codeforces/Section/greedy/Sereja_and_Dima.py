n=int (input())
cards=list(map(int,input().split()))

left = 0
right = n - 1
count_s=0 
count_d=0
for turn in range(n):
    if cards[left] > cards[right]:
        value = cards[left]
        left += 1
    else:
        value = cards[right]
        right -= 1

    if turn % 2 == 0:
        count_s += value
    else:
        count_d += value

print(count_s, count_d)




