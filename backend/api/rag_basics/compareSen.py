from fastapi import APIRouter
from sentence_transformers import SentenceTransformer
from pydantic import BaseModel
from sklearn.metrics.pairwise import cosine_similarity
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

router = APIRouter()

class transformSen(BaseModel):
    query: str

@router.post('/compareSen')
def transformSen(request: transformSen):
    
    print(request.query)
    model = SentenceTransformer("all-MiniLM-L6-v2")
    
    topic = request.query
    
    prompt = ChatPromptTemplate([
        ("system", "You receive a query of a topic and produce a sentence with it"),
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
    
    embedding_respond = model.encode(respond)
    embedding = model.encode(request.query)
    
    similarity = cosine_similarity([embedding], [embedding_respond])[0][0]
    
    return {
    "result": "respond of AI: " + respond + " | Similarity to your text: " + str(similarity)
    }
    
    
    
    
    
    
    
    