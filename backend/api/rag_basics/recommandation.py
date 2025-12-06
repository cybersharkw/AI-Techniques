from fastapi import APIRouter
from sentence_transformers import SentenceTransformer
from pydantic import BaseModel
from sklearn.metrics.pairwise import cosine_similarity
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from numpy import argmax

load_dotenv()

router = APIRouter()

class Recommandation(BaseModel):
    query: str

@router.post('/recommandation')
def transformSen(request: Recommandation):
    
    print(request.query)
    model = SentenceTransformer("all-MiniLM-L6-v2")
    
    topic = request.query
    
    prompt = ChatPromptTemplate([
        ("system", "You receive a query of a topic and produce a 3 Rhymes with it. You must try to use the same words which are given in the topic. Each Sentence must end with . "),
        ("user", "{topic}")
    ])
    
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7,
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )
    
    chain = (
        prompt
        | llm
        | StrOutputParser()
    )
    
    respond = chain.invoke({"topic": topic})
    
    respond_list = []
    
    for i in respond.split("."):
       i = i.strip()
       respond_list.append(i)
        
    #Encode all LLM-responses
    embedding_response = [
        model.encode(respond_list[0]),
        model.encode(respond_list[1]),
        model.encode(respond_list[2])
    ]
    
    embedding = model.encode(request.query)
    #Detect similarites
    similarity = cosine_similarity([embedding], embedding_response)[0]
    
    #Find best matching Index
    best_match_index = similarity.argmax()
    #Receive Score of the best Index
    best_match_score = similarity[best_match_index]
    #Receive best Sentence with the Index
    best_sentence = respond_list[best_match_index]
    
    return {
    "result": "best match" + best_sentence + " | Similarity to your text: " + str(best_match_score)
    }
    
    
    
    
    
    
    
    