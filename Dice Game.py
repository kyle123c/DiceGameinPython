import random

def main():

    playerOne = input('Player One - Please enter your name: ')
    print('Hello, ' + playerOne + '\n')

    playerTwo = input('Player Two - Please enter your name: ')
    print('Hello ' + playerTwo + '\n')

    p1 = 0
    winsPlayer1 = 0
    p2 = 0
    winsPlayer2 = 0
    rounds = 1

    while rounds != 4:
        print('Round ' + str(rounds))
        p1 = roll_dice()
        p2 = roll_dice()
        print(playerOne + 'Roll: ' + str(p1))
        print(playerTwo + 'Roll: ' + str(p2))

        # if , elif, else with a while loop
        if p1 > p2:
            winsPlayer1 = winsPlayer1 + 1
            print(playerOne + ' wins!! \n')
        elif p2 > p1:
            winsPlayer2 = winsPlayer2 + 1
            print(playerTwo + ' wins!! \n')
        else:
            print('Draw \n')

        rounds = rounds + 1
    
    
    if winsPlayer1 > winsPlayer2:
        print(playerOne + ' Wins - Rounds Won: ' + str(winsPlayer1))
    elif winsPlayer2 > winsPlayer1:
        print(playerTwo + ' Wins - Rounds Won: ' + str(winsPlayer2))
    else:
        print('Draw!')

   

def roll_dice():

    dice = random.randint(1,6) # the 6 sides of the dice

    return dice # returning the dice variable





main()