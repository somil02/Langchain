from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.1-8B-Instruct",
    task = 'text-generation'
)

model = ChatHuggingFace(llm = llm)

prompt1 = PromptTemplate(
    template = ' write a detailed report on {topic}',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = 'generate 5 question from  {text}',
    input_variables = ['text']
)

prompt3 = PromptTemplate(
    template = 'give answer for the following question {question}',
    input_variables = ['question']
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser | prompt3 | model | parser

result = chain.invoke({'topic' : 'quantum computing'})

print(result)

chain.get_graph().print_ascii()