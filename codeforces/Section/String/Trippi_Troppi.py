n= int(input())
for _ in range(n):
    strings = input().split()
    array = []
    for i in range(len(strings)):
        array.append(strings[i][0])
        if strings[i]== " ": 
            array.append(strings[i+1])
        
    print("".join(array))