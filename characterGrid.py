someGrid = [
['.','.','.','.','.','.'],
['.','O','O','.','.','.'],
['O','O','O','O','.','.'],
['O','O','O','O','O','.'],
['.','O','O','O','O','O'],
['O','O','O','O','O','.'],
['O','O','O','O','.','.'],
['.','O','O','.','.','.'],
['.','.','.','.','.','.'],
]

def printArt(grid):
  numCols = len(grid[0])
  numRows = len(grid)
  for j in range(numCols):
    for i in range(numRows-1):
      print( grid[i][j],end='')
    print( grid[numRows-1][j])

printArt(someGrid)