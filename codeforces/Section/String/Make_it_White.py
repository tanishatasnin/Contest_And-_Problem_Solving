n= int(input())

for _ in range (n):
    n= int(input())
    s=input()
    

    start=s.find('B')
    end = s.rfind('B')

    print (end-start+1)
    
