import random, sys

print('ROCK, PAPER, SCISSORS \n')

def get_move_name(move):
    if move == 'r':
        return 'Rock'
    elif move == 'p':
        return 'Paper'
    elif move == 's':
        return 'Scissors'

def game():
    wins = 0
    ties = 0
    losses = 0

    # main game loop
    while True:
        print(f'{wins} Wins, {ties} Ties, {losses} Losses')

        # player move loop => handles that only correct inputs are passed forward
        while True:
            player_move = input('Enter your move: (r)ock (p)aper (s)cissors or (q)uit\n')

            if player_move == 'q':
                # Exit game
                # print('FINAL SCORE:' + f'{wins} Wins, {ties} Ties, {losses} Losses')
                print('Exiting game...')
                sys.exit()
            elif player_move == 'r' or player_move == 'p' or player_move == 's':
                break
            
            print('Type one of r, p, s, or q.\n')
            
        random_int = random.randint(1, 3)

        # assign computer_move
        computer_move = ''

        if random_int == 1:
            computer_move = 'r'
        elif random_int == 2:
            computer_move = 'p'
        elif random_int == 3:
            computer_move = 's'

        # print choices
        print(get_move_name(player_move) + ' VS. ' + get_move_name(computer_move))

        # win conditions
        if player_move == computer_move:
            print('It\'s a TIE!')
            ties += 1
        elif player_move == 'r' and computer_move == 'p':
            print('You LOSE!')
            losses += 1
        elif player_move == 'r' and computer_move == 's':
            print('You WIN!')
            wins += 1
        elif player_move == 'p' and computer_move == 's':
            print('You LOSE!')
            losses += 1
        elif player_move == 'p' and computer_move == 'r':
            print('You WIN!')
            wins += 1
        elif player_move == 's' and computer_move == 'r':
            print('You LOSE!')
            losses += 1
        elif player_move == 's' and computer_move == 'p':
            print('You WIN!')
            wins += 1

        print('')


game()