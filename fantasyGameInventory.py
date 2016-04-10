sampleInventory = { 
                    'rope' : 1,
                    'gold coin' : 42,
                    'dagger' : 1,
                    'arrow' : 12,
                    'torch': 6
                  }


def displayInventory(inventory):
  print('Inventory:')
  totalItems = 0
  for k,v in inventory.items():
    print(str(v) + ' ' + k)
    totalItems += v
  print('Total number of items: ' + str(totalItems))

displayInventory(sampleInventory)