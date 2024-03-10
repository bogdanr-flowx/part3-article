from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field

# Instantiate Model
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
)


def call_json_parser():

    #Prompt Template
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Extract information from the following text. \n Formatting instructions: {formatting_instructions}"),
        ("human","{text}")
    ])
    
    class Person(BaseModel):
        name: str = Field(description="The name of the person")
        age: int = Field(description="The age of the person")
    

    parser = JsonOutputParser(pydantic_object=Person)
    
    #Create LLM Chain
    llm_chain = prompt | llm | parser

    
    for text in llm_chain.stream({
            "text": "Generate 5 persons with name and age.", 
            "formatting_instructions":  parser.get_format_instructions()
    }):
        print(text, flush=True)

    
call_json_parser()


