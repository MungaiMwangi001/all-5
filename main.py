import random
print('WELCOME TO THE HANGMAN GAME')

list= ['asterk','jambo','hacker']

choose = random.choice(list)
print(choose)




nilllist = []
for letter in choose:
    nilllist += '_'



num = 0

gameover = False
while not  gameover:
    enter = input("letter: ").lower()

    for position in range(len(choose)):
        letter = choose[position]
        if letter == enter:
          nilllist[position] =letter

    if enter not in  choose:
        num += 1
        guess_left =  7- num
        print(f"you have {guess_left} left" )
        if num >=7:
            print('you loser')
            gameover=True


    print(nilllist)

    if '_'  not in  nilllist:
        print(f"{choose} ,game over,you win")
        gameover= True