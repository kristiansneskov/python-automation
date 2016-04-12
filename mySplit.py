#! python3

def mystrip(text, remove = ''):
  if remove == '':
    #TODO : regex to remove leading whitespace 
    #TODO: regex to remove trailing whitespace 
    text.rstrip()
  return text.lstrip()

print(mystrip('  ge '))