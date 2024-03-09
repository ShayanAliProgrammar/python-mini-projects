import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 5


def generate_code():
    code = []

    for _ in range(CODE_LENGTH):
        code.append(random.choice(COLORS))

    return code


def guess_code():
    while True:
        guess = input("Quess: ").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"\nYou must type {CODE_LENGTH} colors\n")
            continue

        for color in guess:
            if color not in COLORS:
                print(f'\nInvalid color: "{color}". Try again.\n')
                break
        else:
            break

    return guess


def check_code(guess, real_code):
    colors_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in colors_counts:
            colors_counts[color] = 0
        colors_counts[color] += 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            colors_counts[guess_color] -= 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color in colors_counts and colors_counts[guess_color] > 0:
            incorrect_pos += 1
            colors_counts[guess_color] -= 1

    return correct_pos, incorrect_pos


def play_game():
    code = generate_code()
    print(f"Welcome to mastermind, you have {TRIES} to guess the code...")

    # Comment the below line to play this game without (cheating) 😅
    print("\n", *code, "\n")

    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            attempts_str = attempts.__str__()
            print(
                f"\nYou guessed the code in {attempts_str + ' attempt!' if (attempts == 1) else attempts_str + ' attempts'}.\n"
            )
            break

        print(
            f"\nCorrect Positions: {correct_pos} | Incorect Positions: {incorrect_pos}"
        )
    else:
        print("You ran out of attempts, the code was:", *code)


if __name__ == "__main__":
    play_game()
