
d = int(input())
doler_bils = [100 , 20 , 10 , 5 , 1] 

money = 0 
for i in range(len(doler_bils)):
    if d >= doler_bils[i]:
        money += d // doler_bils[i]
        d %= doler_bils[i]

print(money)