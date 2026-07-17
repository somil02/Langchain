from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda
import regex as re

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.1-8B-Instruct",
    task = 'text-generation'
)

model = ChatHuggingFace(llm = llm)

def clean_text(text):
    # Remove emojis and other non-ASCII characters
    text = text.encode("ascii", "ignore").decode()

    # Remove special characters except letters, numbers, spaces and punctuation
    text = re.sub(r"[^a-zA-Z0-9\s.,!?]", "", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text

prompt = PromptTemplate(
    template="""
Write exactly 10 lines about {topic}.

Requirements:
- Include emojis.
- Include special characters like #, @, *, &, %, !.
- Make it interesting.
""",
    input_variables=["topic"]
)

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    'generated_text': RunnablePassthrough(),
    'cleaned_text': RunnableLambda(clean_text)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({'topic':'AI'})

final_result = f"""
Generated Text:
{result['generated_text']}

{'='*50}

Cleaned Text:
{result['cleaned_text']}
"""
print(final_result)