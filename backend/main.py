from fastapi import FastAPI, APIRouter
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from api import langchain


app = FastAPI(
    title="LangChain Patterns API",
    description="Demonstration of key LangChain patterns",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()

# Include routers
app.include_router(langchain.router, prefix="/api/langchain", tags=["Langchain"])
#app.include_router(langgraph.router, prefix="/api/langgraph", tags=["Advanced Langgraph"])

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