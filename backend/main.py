from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .config import get_settings
from .database import get_supabase
from .agents.orchestrator import HealthAgent
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="NutriAI API")
settings = get_settings()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins.split(","),
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

@app.post("/chat")
async def chat(request: ChatRequest, user_id: str):
    # Get user profile for context
    supabase = get_supabase()
    profile = supabase.table("profiles").select("*").eq("id", user_id).single().execute()
    
    agent = HealthAgent()
    response = await agent.process_query(request.message, profile.data)
    
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
