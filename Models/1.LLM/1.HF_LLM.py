from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "LLM-OS-Models/Fabliq-8B-Agent",
    task = "text-generation"
)

result = llm.invoke("write a poem about the moon in 5 lines")
print(result)