from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from fastapi import APIRouter
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

# Request model
class SimpleChainRequest(BaseModel):
    query: str
    temperature: float = 0.7

@router.post("/simple")
async def simple_llm_chain(request: SimpleChainRequest):
    """
    Pattern: Prompt Template -> LLM -> Output Parser
    Most basic LangChain pattern
    """
    
    # Define prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant. Answer the user's question clearly and concisely."),
        ("user", "{query}")
    ])
    
    # Initialize LLM
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7,
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )
    
    # Create chain using LCEL (LangChain Expression Language)
    chain = prompt | llm | StrOutputParser()
    
    # Execute chain
    result = await chain.ainvoke({"query": request.query})
    
    return {"result": result}