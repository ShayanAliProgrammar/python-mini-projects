import random

user_score = 0
computer_score = 0
options = ['rock','paper','scissors']

while True:
    user_input = input('\nType (rock / paper / scissors) or q to quit: ').lower()

    if user_input == 'q':
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_choice = options[random_number]

    user_rock = user_input == 'rock' and computer_choice == 'scissors'
    user_paper = user_input == 'paper' and computer_choice == 'rock'
    user_scissors = user_input == 'scissors' and computer_choice == 'paper'

    if user_rock or user_scissors or user_paper:
        print('You won! 😃')
        user_score += 1

    else:
        print('You lost! 😞')
        computer_score += 1

print(f"\nYou won {user_score} times.")
print(f"The computer won {computer_score} times.")
print(f"Goodbye! 👋")