spam = ['apples', 'bananas', 'tofu', 'cats']

def splitList(list):
  items = ''
  if (len(list) == 0):
    return items
  elif len(list) == 1:
    return list[0]
  else:
    for i in range(len(list)-1):
      items += list[i] + ', '
    items += 'and ' + list[len(list)-1]
  return items

print(splitList(spam))