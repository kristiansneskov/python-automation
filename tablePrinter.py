tableData = [
              ['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose'],
            ]

def printTable(table):
  colWidths = [0] * len(table)
  for i in range(len(table)):
    for j in range(len(table[i])):
      if len(table[i][j]) > colWidths[i]:
        colWidths[i]=len(table[i][j])
  lst3 = []
  for i in range(4):
    lst3.append([item[i] for item in table])
#  print(lst3)
  print(colWidths)
  for i in range(len(lst3)):
    print('')
    for j in range(len(lst3[i])):
      print(lst3[i][j].rjust(colWidths[j]),end=' ')

printTable(tableData)