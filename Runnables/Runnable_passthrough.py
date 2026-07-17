from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.1-8B-Instruct",
    task = 'text-generation'
)

model = ChatHuggingFace(llm = llm)


prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

joke_gen_chain = RunnableSequence(prompt1, model, parser)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'Joke': RunnablePassthrough(),
    'Explaination': RunnableSequence(prompt2, model, parser)
})

result = RunnableSequence(joke_gen_chain, parallel_chain)

print(result.invoke({'topic':'cricket'}))


parallel_chain.get_graph().print_ascii()