import random

# Rock, Paper, Scissors ASCII Art
rock = '''✊'''
paper = '''✋'''
scissors = '''✌️'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))

if user_choice >= 0 and user_choice <= 2:
    print("You chose:")
    print(game_images[user_choice])
else:
    print("You typed an invalid number. You lose!")
    exit()

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice == computer_choice:
    print("It's a draw!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 1 and computer_choice == 0:
    print("You win!")
elif user_choice == 2 and computer_choice == 1:
    print("You win!")
else:
    print("You lose!")
