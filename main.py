import random


def play():
    possible_option = ['rock', 'paper',  'scissor']
    user = input(f"choose any one:rock , paper , scissor:")
    computer = random.choice(possible_option)
    print(f'Computer choice is: {computer}')
    if if_win(user,computer):
        pass

def if_win(yourchoice, computerchoice):
    data = {
        'rock':{'scissor':'win', 'rock':'draw', 'paper':'lose'},
        'paper':{'rock':'win', 'paper':'draw', 'scissor':'lose'},
        'scissor':{'paper':'win','scissor':'draw', 'rock':'lose'}

    }
    yourscore = data[yourchoice][computerchoice]
    computerscore = data[computerchoice][yourchoice]
    if yourscore == 'win':
        print('Congrats! You win')
    elif yourscore == 'draw':
        print('It`s a tie ')
    else:
        print('You lose')

play()
