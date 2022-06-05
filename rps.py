import random
import math
from unittest import result

def play():
    user = input("what's your choice? 'R' for rock, 'P' for paper, 'S' for scissors\n")
    user = user.upper()

    computer = random.choice(['R', 'P', 'S'])
    if user == computer:
        return (0, user, computer)

    # r > s, s > p, p > r    
    if is_win(user, computer):
        return (1, user, computer)

    return (-1, user, computer)
    

def is_win(player, opponent):
    # return if the player beats the opponent
    # winning condition: r > s, s > p, p > r 
    if (player == 'R' and opponent == 'S') or (player == 'S' and opponent == 'P') or (player == 'P' and opponent == 'R'):
        return True
    return False

def play_best_of(n):
    # play against the computer until someone wins best of n games
    # to win, you must win cell(n/2) games (ie 2/3, 3/5, 4/7)
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = play()
        # tie
        if result == 0:
            print('it is a tie. You and the computer have both chosen {}.\n'.format(user))
        # yoou win
        elif result == 1:
            player_wins += 1
            print('You chose {} and the computer chose {}. You won!\n'.format(user, computer))
        else:
            computer_wins += 1
            print('You chose {} and the computer chsose {}. You lost :(\n'.format(user, computer))
        print('\n')

    if player_wins > computer_wins:
        print('You have won the best of {} games! What a champ :D'.format(n))
    else:
        print('Unfortunately, the computer has won the best of {} games. Better luck next time')

if __name__ == '__main__':
    play_best_of(3) # 2
    play_best_of(9) # 5