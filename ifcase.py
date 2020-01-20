#There is no switch statement in python
#YOu can have an else block for a while loop. When the while condition is false, the else block will be executed.
number = 23
guess = int(input('Enter an integer : '))

if guess == number:
  print ('You got it')
elif guess < number:
  print ('A little higher')
else: 
  print ('A little lower')

print 'DONE'
