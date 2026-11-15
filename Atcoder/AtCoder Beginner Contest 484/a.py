b , r =map(int,input().split())
row=30
col=30
if b>row or r>col:
    print("0") ; 
else: 
    pieces_of_chocolate_remain = (row-b )*(col-r)
    print(pieces_of_chocolate_remain) 