n=int(input())
balls=list(map(int,input().split()))
 
sorted_balls=sorted(balls)
sorted_reverse_balls=sorted(balls,reverse=True)
if sorted_reverse_balls[0] == 9:
    print(sorted_balls[0])
else:
    print(-1)