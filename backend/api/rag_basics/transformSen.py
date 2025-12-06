from fastapi import APIRouter
from sentence_transformers import SentenceTransformer
from pydantic import BaseModel


router = APIRouter()

class transformSen(BaseModel):
    query: str

@router.post('/transformSen')
def transformSen(request: transformSen):
    
    print(request.query)
    model = SentenceTransformer("all-MiniLM-L6-v2")
    
    embedding = model.encode(request.query)
    
    return {"result": embedding.tolist()}
    
    
    
    
    
    
    
    