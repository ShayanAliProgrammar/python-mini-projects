import random
from helpers import get_num_input

playing = input("Do you want to play? (Y/n): ").lower()

while playing not in {"y", "n", "\n", ""}:
    playing = input("Would you like to play? (Y/n): ").lower()


if playing == "n":
    quit()

min_num = get_num_input('\nEnter a minimum number: ')
max_num = get_num_input('\nEnter a maximum number: ')

# random_number = random.randrange(0, 11) # random number between 0 to 10
random_number = random.randint(min_num, max_num) # random number between min to max

attempts = 0

while attempts != 9:
    guessed_number = get_num_input('\nGuess the number: ')

    guessed_number = int(guessed_number)

    if (guessed_number == random_number):
        print(f'You guessed the number 🎉 in {attempts} attempts')

        break

    elif guessed_number >= random_number:
        print('You guessed higher number')

    elif guessed_number <= random_number:
        print('You guessed lower number')

    attempts += 1
    