import random


actions = ('rock', 'paper', 'scissors')
running = True

while running:

    player = None
    comp = random.choice(actions)

    while player not in actions:
        player = input('Rock/Paper/Scissors: ')

    print(f'Player: {player}')
    print(f'Computer: {comp}')

    if player.lower() == comp:
        print('Its a tie')
    elif player.lower() == 'rock' and comp == "scissors":
        print('You win!')
    elif player.lower() == 'paper' and comp == 'rock':
        print('You win')
    elif player.lower() == 'scissors' and comp == 'paper':
        print('You win!')
    else:
        print('You lose')
   
    play_again = input('Play again? (y/n): ')
    if play_again.lower() != 'y':
        running = False

print('Thanks for playing!')