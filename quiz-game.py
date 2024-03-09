from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

print("Welcome to the quiz game")

playing = input("Do you want to play? (Y/n): ").lower()

while playing not in {"y", "n", "\n", ""}:
    playing = input("Would you like to play? (Y/n): ").lower()


if playing == "n":
    quit()

print("\nAlright, let's begin. 😊")

questions = []
score = 0

llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7)
instructions_str = """
1. Generate a minimum of 5 and a maximum of 5 random questions along with their answers.

2. The final expression should be a Python expression that can be called with the `eval()` function.

3. PRINT ONLY THE EXPRESSION.

4. Do not quote the expression.

5. Return all the questions/answers in this format (text format only): [ { 'question': 'INSERT YOUR QUESTION', 'answer': 'INSERT YOUR ANSWER' }, { 'question': 'INSERT YOUR QUESTION', 'answer': 'INSERT YOUR ANSWER' }, ... ] Replace those three dot to actual questions and answers.
"""

prompt_str = """You are working in quiz game using Python.
            You have to follow these instructions to generate some questions.

            Follow these instructions:
            {instructions_str}

            Query: {query}

            Expression: """

prompt = PromptTemplate.from_template(prompt_str)
formated_prompt = prompt.format_prompt(
    instructions_str=instructions_str,
    query="Let's generate some easy level questions&answers for these topics: Python.",
)

print("Generating some questions. 😃\n\n")

questions = eval(llm.invoke(formated_prompt).content)
answers = []

index = 1

for ques in questions:
    answer = input(f"Question {index}: {ques["question"]}\nAnswer: ")
    while answer == "" or answer == "\n":
        answer = input(f"Question {index}: {ques["question"]}\nAnswer: ")

    answers.append(answer)
    index += 1
    print()

index = 0

for answer in answers:
    question = questions[index].get("question")

    res = llm.invoke(
        f"Answer yes if user selected answer 55% matches to correct answer otherwise return no. QUERY: Is this '{answer}' user selected answer matches or does not matches based on these fields:\n\nQUESTION: {question}\n\nCORRECT ANSWER: {questions[index].get('answer')}."
    ).content

    if res == "yes":
        score += 1
    else:
        print(f'Wrong answer for question no ❌: {1+index}\nHere this currect answer ✅: {questions[index]['answer']}\n')
    index += 1

print(f"Your score: {score.__str__()}")
