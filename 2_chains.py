from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Instantiate Model
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
)

#Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "Generate a list of 5 synonys for the following world. Return the list as a comma separated list."),
    ("human","{input}")
])

#Create LLM Chain
llm_chain = prompt | llm

response = llm_chain.invoke({"input": "happiness"})

print(response)
