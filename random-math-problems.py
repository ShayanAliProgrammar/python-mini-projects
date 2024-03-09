import random
import time
from helpers import get_num_input

OPERATORS = ['+', '-', '*']
MIN_OPERAND = 2
MAX_OPERAND = 3
TOTAL_PROBLEMS = 10
user_score = 0

def generate_expression():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)

    operator = random.choice(OPERATORS)

    expression = f"{str(left)} {str(operator)} {str(right)}"
    answer = eval(expression)
    return expression, answer


current_problem_index = 0

print('--------------------------')

start_time = time.time()

while current_problem_index <= TOTAL_PROBLEMS:
    expression, answer = generate_expression()

    user_input = get_num_input(f"\nProblem # {1+current_problem_index}\n{expression} = ")

    if (user_input == answer):
        user_score +=1
    
    current_problem_index+=1

total_time = time.time() - start_time

print('--------------------------')

print(f'You finished {TOTAL_PROBLEMS} problems in {round(total_time, 2)} seconds')
print(f'Score: {user_score}')