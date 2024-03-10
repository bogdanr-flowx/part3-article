from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
)

response = llm.batch(["Hello, who are you?","Write me a joke about AI"])

print(response)

stream = llm.stream("Tell me a joke about AI")

for chunk in stream:
    print(chunk.content, end="", flush=True)