import random

Easy_level_turn = 10
Hard_level_turn = 5

def check_answer(user_guess, actual_guess, turns):
    if user_guess < actual_guess:
        print("Too low")
        return turns - 1

    elif user_guess > actual_guess:
        print("Too high")
        return turns - 1

    else:

        print(f"You got it! The answer was {actual_guess}")


def set_difficulty():
    choose_diff = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if choose_diff == "easy":
        return Easy_level_turn

    else:
        return Hard_level_turn


def play_game():
    from art import logo
    print(logo)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1,100)

    turns = set_difficulty()


    guess = 0
    while turns != 0:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if guess == answer:
            return

        if turns == 0:
            print("You've run out of guesses, you lose.")
            return

        elif guess != answer:
            print("Guess again.")

play_game()