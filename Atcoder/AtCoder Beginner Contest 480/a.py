grid = [input().strip() for _ in range(2)]

if (grid[0][0] == 'A' and grid[0][1] == 'D') or \
   (grid[0][0] == 'D' and grid[0][1] == 'A') or \
   (grid[1][0] == 'A' and grid[1][1] == 'D') or \
   (grid[1][0] == 'D' and grid[1][1] == 'A') or \
   (grid[0][0] == 'A' and grid[1][0] == 'D') or \
   (grid[0][0] == 'D' and grid[1][0] == 'A') or \
   (grid[0][1] == 'A' and grid[1][1] == 'D') or \
   (grid[0][1] == 'D' and grid[1][1] == 'A'):
    print("Yes")
else:
    print("No")