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
    item = pyperclip.paste()
  elif keyword == 'delete':
    print('delete item ' + sys.argv[1].lower())
elif len(sys.argv) == 2:
  pyperclip.copy(str(list(mcbShelf.keys())))

mcbShelf.close()