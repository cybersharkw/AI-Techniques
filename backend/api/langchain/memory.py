from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from fastapi import APIRouter
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from fastapi.concurrency import run_in_threadpool
load_dotenv()

router = APIRouter()

checkpointer = InMemorySaver()
 
# Request model
class MemoryChainRequest(BaseModel):
    query: str
    thread_id: str = "default"

@router.post("/memory")
async def memory_llm_chain(request: MemoryChainRequest):
    
   
    agent = create_agent(
        "gpt-3.5-turbo",
        tools=[],
        checkpointer=checkpointer,
        context_schema="update"
        )
        
    result = agent.invoke(
            {"messages": [{"role": "user", "content": request.query}]},
            {"configurable": {"thread_id": 1}},)
         
    ai_message = result["messages"][-1]
    
    return {"result": ai_message.content }
        