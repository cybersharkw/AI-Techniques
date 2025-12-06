from fastapi import APIRouter
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

router = APIRouter()

class PdfQuery(BaseModel):
    query: str


# In-memory storage for embeddings and text chunks
_chunks = []
_embeddings = None
_model = None


def initialize_pdf():
    """Load and process PDF into memory"""
    global _chunks, _embeddings, _model
    
    if len(_chunks) > 0:
        return  # Already initialized
    
    # Load PDF
    loader = PyPDFLoader("../../assets/pdf/Introduction_pytorch.pdf")
    pages = loader.load()

    # Extract text
    full_text = "\n".join([p.page_content for p in pages])

    # Chunk PDF
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    _chunks = splitter.split_text(full_text)

    # Create embeddings
    _model = SentenceTransformer("all-MiniLM-L6-v2")
    _embeddings = _model.encode(_chunks)


@router.post("/pdfSearch")
def pdf_search(request: PdfQuery):
    """Search through PDF using in-memory vector storage"""
    
    try:
        # Initialize PDF on first call
        initialize_pdf()
        
        # Encode query
        query_embedding = _model.encode([request.query])
        
        # Calculate cosine similarity
        similarities = cosine_similarity(query_embedding, _embeddings)[0]
        
        # Get top 3 results
        top_indices = np.argsort(similarities)[::-1][:3]
        
        results = []
        for idx in top_indices:
            results.append({
                "text": _chunks[idx],
                "score": float(similarities[idx])
            })
        
        return {
            "status": "success",
            "query": request.query,
            "results": results
        }
    
    except Exception as e:
        return {
            "status": "fail",
            "message": f"Error: {str(e)}"
        }