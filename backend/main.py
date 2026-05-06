import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import get_supabase
from agents.orchestrator import HealthAgent
from utils.cloud_security import RateLimitMiddleware, google_cloud_logger
from pydantic import BaseModel, constr

app = FastAPI(title="Health.AMD Protocol")

app.add_middleware(RateLimitMiddleware, limit=30, window=60)
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("CORS_ORIGINS", "*").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    lat: float = 12.9716
    lng: float = 77.5946

@app.get("/")
async def root():
    return {"message": "NutriAI Backend is live"}

@app.get("/profile")
async def get_profile(user_id: str):
    supabase = get_supabase()
    response = supabase.table("profiles").select("*").eq("id", user_id).single().execute()
    return response.data

from sse_starlette.sse import EventSourceResponse
import asyncio

@app.post("/chat")
async def chat(request: ChatRequest, user_id: str):
    supabase = get_supabase()
    profile = supabase.table("profiles").select("*").eq("id", user_id).single().execute()
    
    agent = HealthAgent()
    
    async def event_generator():
        # This is a simplified streaming loop for demo purposes
        # In a real app, you would yield chunks from the OpenAI stream
        response_text = await agent.process_query(request.message, profile.data)
        
        # Simulate streaming by chunking the final response
        for chunk in response_text.split(" "):
            yield {"data": chunk + " "}
            await asyncio.sleep(0.05)
            
    return EventSourceResponse(event_generator())

if __name__ == "__main__":
    import os
    import uvicorn

    port = int(os.getenv("PORT", "8000"))
    uvicorn.run(app, host="0.0.0.0", port=port)
