from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embedding = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

document = [
    # Cricket (Similar)
    "Virat Kohli is one of India's greatest batsmen. He has scored many centuries in international cricket and is known for his aggressive style of play.",
    "Virat Kohli has represented India in all formats of cricket. His consistency and fitness have made him one of the best modern-day batsmen.",
    "MS Dhoni is a legendary Indian captain who led India to victory in the 2011 Cricket World Cup. He is famous for his calm leadership and wicketkeeping skills.",
    "Cricket is one of the most popular sports in India. Millions of fans watch international matches and support their favorite teams.",

    # Movies (Similar)
    "The movie 3 Idiots is based on engineering college life. It teaches students to focus on learning instead of chasing marks.",
    "3 Idiots is a comedy-drama film starring Aamir Khan. The movie became one of the biggest hits in Bollywood.",
    "Dangal is a sports drama inspired by the life of wrestler Mahavir Singh Phogat and his daughters.",
    "Bollywood produces hundreds of movies every year across different genres such as action, comedy, romance, and drama.",

    # Music
    "Arijit Singh is one of India's most popular playback singers. His soulful voice has made many songs unforgettable.",
    "Lata Mangeshkar was known as the Nightingale of India. She recorded thousands of songs during her remarkable career.",
    "Music has the power to reduce stress, improve mood, and connect people across cultures.",

    # Technology
    "Artificial Intelligence enables computers to perform tasks that normally require human intelligence, such as language understanding and image recognition.",
    "Machine learning is a branch of artificial intelligence where algorithms learn patterns from data without explicit programming.",
    "Deep learning uses neural networks with multiple layers to solve complex problems like speech recognition and computer vision.",
    "Python is one of the most popular programming languages for artificial intelligence and data science.",

    # Space
    "The Solar System consists of the Sun and the planets that orbit around it, including Earth, Mars, and Jupiter.",
    "Mars is often called the Red Planet because of its reddish appearance caused by iron oxide on its surface.",
    "NASA conducts space exploration missions to study planets, stars, and distant galaxies.",

    # Health
    "Regular exercise improves cardiovascular health, strengthens muscles, and helps maintain a healthy body weight.",
    "Eating fruits and vegetables every day provides essential vitamins, minerals, and dietary fiber.",
    "Drinking enough water throughout the day helps maintain proper hydration and supports overall health.",

    # Animals
    "Dogs are loyal and intelligent animals that have lived alongside humans for thousands of years.",
    "Cats are independent pets known for their agility, curiosity, and playful behavior.",
    "Elephants are the largest land animals and are famous for their intelligence and strong family bonds.",

    # Travel
    "Paris is one of the most visited cities in the world because of landmarks such as the Eiffel Tower and the Louvre Museum.",
    "Japan attracts millions of tourists every year with its blend of modern cities, ancient temples, and beautiful landscapes.",
    "Traveling allows people to experience new cultures, foods, and traditions.",

    # Finance
    "Investing in stocks can help grow wealth over the long term, although it also involves financial risk.",
    "Banks provide services such as savings accounts, loans, and online banking facilities.",
    "Personal finance involves budgeting, saving money, and making informed investment decisions."
]


query = "What is quantum computing?"
doc_embedding = embedding.embed_documents(document)
query_embedding = embedding.embed_query(query)

similarity_score = cosine_similarity([query_embedding],doc_embedding)[0]
index, score = sorted(list(enumerate(similarity_score)), key = lambda x:x[1],reverse = True)[0]

print("query: ",query)
print("document: ",document[index])
print("similarity: ", score)

