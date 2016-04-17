#! /usr/bin/env python3
# mcb.pyw - Saves and loads pieces of text to the clipboard
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
   #        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
   #        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3:
  keyword = sys.argv[1].lower()
  item = sys.argv[2].lower()
  if keyword == 'save':
    mcbShelf[item] = pyperclip.paste()
  elif keyword == 'delete':
    if item in mcbShelf:
      del mcbShelf[item]
    else:
      print('item ' + item + ' not stored.')
  
elif len(sys.argv) == 2:
  if sys.argv[1].lower() == 'list':
    pyperclip.copy(str(list(mcbShelf.keys())))
  elif sys.argv[1] in mcbShelf:
    pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()