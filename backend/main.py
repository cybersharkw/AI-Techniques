from fastapi import FastAPI, APIRouter
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from api.langchain import simple_router, sequential_router, memory_router
from api.rag_basics import transformSen_router, compareSen_router, recommandation_router, pdfSearch_router

app = FastAPI(
    title="LangChain Patterns API",
    description="Demonstration of key LangChain patterns",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()

# Include routers
app.include_router(simple_router, prefix="/api/langchain", tags=["Langchain"])
app.include_router(sequential_router, prefix="/api/langchain", tags=["Langchain"])
app.include_router(memory_router, prefix="/api/langchain", tags=["Langchain"])

app.include_router(transformSen_router, prefix="/api/rag-basics", tags=["Rag-Basics"])
app.include_router(compareSen_router, prefix="/api/rag-basics", tags=["Rag-Basics"])
app.include_router(recommandation_router, prefix="/api/rag-basics", tags=["Rag-Basics"])
app.include_router(pdfSearch_router, prefix="/api/rag-basics", tags=["Rag-Basics"])

@app.get("/")
async def root():
    """Redirect to interactive API documentation"""
    return RedirectResponse(url="/docs")

@app.get("/health")
async def health_check():
    """
    Health check endpoint for monitoring
    Used by load balancers, Docker, Kubernetes, etc.
    """
    return {
        "status": "healthy",
        "service": "langchain-api",
        "version": "1.0.0"
    }