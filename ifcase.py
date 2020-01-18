number = 23
guess = int(input('Enter an integer : '))

if guess == number:
  print ('You got it')
elif guess < number:
  print ('A little higher')
else: 
  print ('A little lower')

print 'DONE'
