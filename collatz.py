def collatz(number):
  newNumber = 0
  if number % 2 == 0:
    newNumber = number / 2
  else:
    newNumber = 3*number +1 
  print(str(int(newNumber)))
  return newNumber  


print('Welcome to collatz')
print('Please type a positive integer')
try:
  currentNumber = int(input())
  while currentNumber != 1:
    currentNumber=collatz(currentNumber)
  print('You have converged')
except ValueError:
  print('Invalid input')