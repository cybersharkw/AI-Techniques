from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from fastapi import APIRouter
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

# Request model
class SequentialChainRequest(BaseModel):
    query: str  # Changed from 'topic' to match your model
    temperature: float = 0.7

# OPTION 1: Modern LCEL approach (RECOMMENDED - No deprecation warnings)
@router.post("/sequential")
async def sequential_llm_chain(request: SequentialChainRequest):
    """
    Sequential chain using modern LCEL (LangChain Expression Language)
    1. Takes a query and generates a creative title
    2. Uses that title to write content about it
    """
    
    # Initialize LLM
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=request.temperature,
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )
    
    # Step 1: Generate title from query
    title_prompt = ChatPromptTemplate.from_messages([
        ("system", "Generate a creative and engaging title for the given topic."),
        ("user", "{query}")
    ])
    
    # Step 2: Generate content from title
    content_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a content creator. Write three engaging sentences about the given title."),
        ("user", "Title: {title}\n\nWrite three sentences:")
    ])
    
    # Create sequential chain using pipe operator
    # query -> title_prompt -> llm -> extract text -> content_prompt -> llm -> extract text
    chain = (
        {"query": lambda x: x["query"]}  # Pass through query
        | title_prompt 
        | llm #send prompt
        | StrOutputParser()  # Extract title as string
        | (lambda title: {"title": title})  # Prepare for next step
        | content_prompt 
        | llm 
        | StrOutputParser()  # Extract final content
    )
    
    # Execute the chain
    result = await chain.ainvoke({"query": request.query})
    
    return {
        "result": result,
        "query": request.query,
        "method": "LCEL (modern)"
    }