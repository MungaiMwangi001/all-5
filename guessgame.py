import random

''' the game is to :
# guesss a number
#comp gots a number
#if gueessed = comp guess
then congratulations


'''
n = 20
guessed_num   = int(n*random.random()) + 1
print(guessed_num)

guess = 0
while   guess  !=  guessed_num:
        guess = int(input('weka number nani: '))
        if guess > 0 :

           if guess > guessed_num:
               print('shuka kidogo')
           elif guess < guessed_num:
               print('panda kidogo')
        else:
               print('you giving up  my guy')
               break

else:
           print('congratulations, wee bana')