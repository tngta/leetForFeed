grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

if not grid:
    print(0)

rows = len(grid)
cols = len(grid[0])
count = 0

def dfs(r,c):
    if r<0 or c<0 or r>rows-1 or c>cols-1 or grid[r][c]=="0":
        return
    
    # Mark as visited
    grid[r][c] = "0"

    dfs(r+1, c)
    dfs(r-1, c)
    dfs(r, c+1)
    dfs(r, c-1)

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "1":
            count += 1
            dfs(r, c)

print(count)