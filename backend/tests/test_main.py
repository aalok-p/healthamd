import pytest
from fastapi.testclient import TestClient
from main import app
from agents.orchestrator import HealthAgent

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "NutriAI Backend is live"}

def test_profile_endpoint_missing():
    # Test for 404 when user profile not found
    # (Note: In a real test, we would mock the Supabase client)
    pass

@pytest.mark.asyncio
async def test_agent_initialization():
    agent = HealthAgent()
    assert agent.model is not None
    assert agent.mcp is not None

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
