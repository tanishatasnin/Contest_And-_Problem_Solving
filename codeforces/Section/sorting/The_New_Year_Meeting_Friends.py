x1, x2, x3 = map(int, input().split()) # 7 1 4 
min_time = min((abs(x1 - x2) + abs(x1 - x3)), (abs(x2 - x1) + abs(x2 - x3)), (abs(x3 - x1) + abs(x3 - x2))) 
print(min_time)

