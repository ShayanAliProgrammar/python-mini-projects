from model import model
from langchain.schema import HumanMessage

messages = [
    HumanMessage(content="from now you are Python Gemini"),
    HumanMessage(content="who are you?"),
    HumanMessage(content="what is your name?"),
]

result = model.invoke(messages)
print(result.content)
