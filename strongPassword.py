import re
pwRegex = re.compile(r'''(
  ^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$
  )''', re.VERBOSE)

aPw = 'fefffERerrEE3'


if (len(pwRegex.findall(aPw))):
  print('Password is deemed valid')
else:
  print('invalid password')