
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# ---------------- Embedding Model ----------------
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ---------------- Documents ----------------
documents = [
    "Virat Kohli is one of India's greatest batsmen. He has scored many centuries in international cricket and is known for his aggressive style of play.",
    "Virat Kohli has represented India in all formats of cricket. His consistency and fitness have made him one of the best modern-day batsmen.",
    "MS Dhoni is a legendary Indian captain who led India to victory in the 2011 Cricket World Cup. He is famous for his calm leadership and wicketkeeping skills.",
    "Cricket is one of the most popular sports in India. Millions of fans watch international matches and support their favorite teams.",

    "The movie 3 Idiots is based on engineering college life. It teaches students to focus on learning instead of chasing marks.",
    "3 Idiots is a comedy-drama film starring Aamir Khan. The movie became one of the biggest hits in Bollywood.",
    "Dangal is a sports drama inspired by the life of wrestler Mahavir Singh Phogat and his daughters.",
    "Bollywood produces hundreds of movies every year across different genres such as action, comedy, romance, and drama.",

    "Arijit Singh is one of India's most popular playback singers. His soulful voice has made many songs unforgettable.",
    "Lata Mangeshkar was known as the Nightingale of India. She recorded thousands of songs during her remarkable career.",
    "Music has the power to reduce stress, improve mood, and connect people across cultures.",

    "Artificial Intelligence enables computers to perform tasks that normally require human intelligence, such as language understanding and image recognition.",
    "Machine learning is a branch of artificial intelligence where algorithms learn patterns from data without explicit programming.",
    "Deep learning uses neural networks with multiple layers to solve complex problems like speech recognition and computer vision.",
    "Python is one of the most popular programming languages for artificial intelligence and data science."
]

# ---------------- Embed Documents Once ----------------
doc_embeddings = np.array(embedding.embed_documents(documents))

# ---------------- Load TinyLlama ----------------
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=200,
    temperature=0.3,
    do_sample=False,
)

llm = HuggingFacePipeline(pipeline=pipe)

# ---------------- Query ----------------
query = input("Enter your question: ")

query_embedding = np.array(embedding.embed_query(query))

scores = cosine_similarity(
    query_embedding.reshape(1, -1),
    doc_embeddings
)[0]

# ---------------- Retrieve Top-3 ----------------
top_k = 3
threshold = 0.45

top_results = sorted(
    enumerate(scores),
    key=lambda x: x[1],
    reverse=True
)[:top_k]

context = ""

for idx, score in top_results:
    if score >= threshold:
        context += documents[idx] + "\n\n"

# ---------------- Prompt ----------------
if context:
    prompt = f"""
You are a helpful assistant.

Answer the question ONLY using the context below.

Context:
{context}

Question:
{query}

Answer:
"""
else:
    prompt = f"""
Answer the following question.

Question:
{query}

Answer:
"""

# ---------------- Generate ----------------
response = llm.invoke(prompt)

print("\n==============================")
print(response)
print("==============================")