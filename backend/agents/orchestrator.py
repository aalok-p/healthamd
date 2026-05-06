import json
import google.generativeai as genai
from typing import List, Dict, Any
from ..config import get_settings
from ..mcp.client import MockSwiggyMCP
from ..mcp.tools import tools

class HealthAgent:
    def __init__(self):
        settings = get_settings()
        genai.configure(api_key=settings.gemini_api_key)
        self.model = genai.GenerativeModel(
            model_name="gemini-2.0-flash",
            tools=tools
        )
        self.mcp = MockSwiggyMCP()
        self.chat = self.model.start_chat(enable_automatic_function_calling=True)

    async def process_query(self, query: str, user_profile: Dict[str, Any]) -> str:
        system_prompt = f"""
        You are NutriAI, a health-focused Swiggy assistant.
        User Profile:
        - Calorie Goal: {user_profile.get('calorie_goal')}
        - Allergies: {user_profile.get('allergies')}
        - Dietary Prefs: {user_profile.get('dietary_preferences')}
        
        Your job is to help users find healthy food on Swiggy Food or groceries on Instamart.
        Always explain WHY a choice is healthy based on their goals.
        Use tools to search and retrieve live data.
        """
        
        # In a real app, you'd handle the function calling loop manually or via automatic mode
        # Since we use MockSwiggyMCP, we need to map the tool calls to our mock methods.
        
        response = self.chat.send_message(f"{system_prompt}\n\nUser: {query}")
        
        # Handle tool calls (simplified for brevity in this example)
        # Note: Gemini 2.0 automatic function calling handles the loop if tools are passed correctly
        # and the functions are provided to the model.
        
        return response.text

    def get_tool_map(self):
        return {
            "food_search_restaurants": self.mcp.search_restaurants,
            "food_get_menu": self.mcp.get_menu,
            "im_search_grocery": self.mcp.search_grocery,
        }
