import random

def play():
    user_choice = input("Please enter 'r' for rock, 'p' for paper and 's' for scissors:  ")
    comp_choice = random.choice(['r', 'p', 's'])

    if user_choice == comp_choice:
        return 'It\'s a tie'

    if isWin(user_choice, comp_choice):
        return "You won!"

    return "You lost!"

def isWin(player, opponent):
    if(player =="r" and opponent =="s") or (player =="s" and opponent == "p") or (player =="p" and opponent == "r"):
        return True
    
print(play())