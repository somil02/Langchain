#In new version of langchain v1.0 + this is removed you have to use pydantic for structured output

from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.1-8B-Instruct",
    task = 'text-generation'
)

model = ChatHuggingFace(llm = llm)

schema = [
    ResponseSchema(name="fact1", description="The first fact about the topic"),
    ResponseSchema(name="fact2", description="The second fact about the topic"),
    ResponseSchema(name="fact3", description="The third fact about the topic"),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give 3 fact about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)