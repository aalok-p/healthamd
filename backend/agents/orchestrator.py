import json
from openai import OpenAI
from typing import List, Dict, Any
from ..config import get_settings
from ..mcp.client import MockSwiggyMCP
from ..mcp.tools import tools

class HealthAgent:
    def __init__(self):
        settings = get_settings()
        self.client = OpenAI(
            api_key=settings.oxlo_api_key,
            base_url=settings.oxlo_base_url
        )
        self.model = settings.oxlo_model
        self.mcp = MockSwiggyMCP()
        self.tool_map = {
            "food_search_restaurants": self.mcp.search_restaurants,
            "food_get_menu": self.mcp.get_menu,
            "im_search_grocery": self.mcp.search_grocery,
        }

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
        
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query}
        ]
        
        # Tool-calling loop
        for _ in range(5):  # Max 5 turns to prevent infinite loops
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=tools,
                tool_choice="auto"
            )
            
            message = response.choices[0].message
            messages.append(message)
            
            if not message.tool_calls:
                return message.content
            
            for tool_call in message.tool_calls:
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)
                
                # Call the mock MCP tool
                tool_func = self.tool_map.get(function_name)
                if tool_func:
                    # Note: Mock functions are async, so we await them
                    result = await tool_func(**function_args)
                    
                    messages.append({
                        "tool_call_id": tool_call.id,
                        "role": "tool",
                        "name": function_name,
                        "content": json.dumps(result)
                    })
                else:
                    messages.append({
                        "tool_call_id": tool_call.id,
                        "role": "tool",
                        "name": function_name,
                        "content": "Tool not found"
                    })
        
        return "I'm sorry, I encountered an issue while searching for healthy options."
