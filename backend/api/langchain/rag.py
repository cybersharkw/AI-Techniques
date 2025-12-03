




#Vectorize message

#visualize Vectors

#hugginface sentence Transformers
""" from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

sentence="My computer is the very best"

sentences = [
    "i live in quepos",
    "quepos is very beautiful",
    "i like food"
]

embeddings = model.encode(sentences)
print(embeddings.shape)

similarities = model.similarity(embeddings, embeddings)
print(similarities) """

#compare sentences 
""" from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

sentence="My computer is the very best"

sentences = [
    "i live in quepos",
    "quepos is very beautiful",
    "My computer is the very best"
]

embedding = model.encode(sentence)
embeddings = model.encode(sentences)


similarities = model.similarity(embeddings, embeddings)
#print(similarities)

em = embedding.reshape(1,-1)
cosin_sim = cosine_similarity(em, embeddings, dense_output=True)

best_match = cosin_sim[0].argmax()
print(sentences[best_match]) """

#recommandation System
""" import faiss
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "i live in quepos",
    "quepos is very beautiful",
    "My computer is the very best"
]

# Encode all sentences
embeddings = model.encode(sentences).astype("float32")

# Create index
dim = embeddings.shape[1]
index = faiss.IndexFlatL2(dim)

# Add embeddings
index.add(embeddings)

# Query
query = "My computer is the very best"
query_vec = model.encode([query]).astype("float32")

# Search
D, I = index.search(query_vec, k=1)

best_match = sentences[I[0][0]]
print("Best match:", best_match) """