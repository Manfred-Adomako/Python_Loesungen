#Cracking numbers
import random

number = random.randrange(0, 100)
x = int(input('Guess a number between 0 and 100: '))

count = 5

while count > 1:

    count -= 1

    if x > number:
        print ('Please try a lower number.' + " Tries left:  " + str(count))
        x = int(input('Guess again:  '))
        
    elif x < number:
        print('Pleae try a higher number.' + " Tries left:  " + str(count))
        x = int(input('Guess again:  '))
        
    else:
        print ("Right Answer")

if count == 1:
    print ("Game Over")
