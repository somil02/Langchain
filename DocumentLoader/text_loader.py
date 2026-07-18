from langchain_community.document_loaders import TextLoader
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = 'meta-llama/Llama-3.1-8B-Instruct',
    task = "text-generation",
)

model = ChatHuggingFace(llm = llm)

prompt = PromptTemplate(
    template = "write a summary for following poem - \n {poem}",
    input_variables = ['poem']
)

loader = TextLoader("cricket.txt", encoding = 'utf-8')

docs = loader.load()

parser = StrOutputParser()

chain =  prompt | model | parser

result = chain.invoke({'poem':docs[0].page_content})

print(result)