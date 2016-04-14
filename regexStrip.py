#! python3

import re,sys
def regexStrip(text, remove = ''):
  regexWs = re.compile(r'''(
    (^\s*)(.*[^\s])(\s*)$
    )''', re.VERBOSE)

  match = regexWs.findall(text)
  strippedText = ''
  if len(match)==1:
    groups = match[0]
    strippedText = ''.join(groups[2:len(groups)-1])
  else:
    return strippedText

  if remove != '':
    removeRegex = re.compile(remove)
    return removeRegex.sub('',strippedText)
  return strippedText

response = ''
if len(sys.argv) == 2:
  response = regexStrip(sys.argv[1])
elif (len(sys.argv) == 3):
  response = regexStrip(sys.argv[1], sys.argv[2])
else:
  response = 'Please specify one or two strings as argument'
print('|' + response + '|')