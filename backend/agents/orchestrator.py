import json
from openai import OpenAI
from typing import List, Dict, Any
from config import get_settings
from mcp.client import MockSwiggyMCP
from mcp.tools import tools

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
        You are NutriAI Protocol, a high-performance health optimization agent.
        
        USER CONTEXT:
        - CALORIE TARGET: {user_profile.get('calorie_goal')}
        - ALLERGENS: {user_profile.get('allergies')}
        - DIETARY PREFERENCES: {user_profile.get('dietary_preferences')}
        
        OPERATIONAL PROTOCOL:
        1. ANALYZE: Evaluate the request against the USER CONTEXT.
        2. SCORE: For every food recommendation, provide a [HEALTH SCORE: 0-100] based on macro-alignment.
        3. ORCHESTRATE: If a dish is unavailable on Swiggy Food, automatically pivot to Instamart to find ingredients.
        4. JUSTIFY: Explain the scientific reason for each recommendation (e.g., glycemic index, protein density).
        
        Always maintain a professional, technical, and precise tone.
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
                
                tool_func = self.tool_map.get(function_name)
                if tool_func:
                    result = await tool_func(**function_args)
                    
                    # If no results found, provide a nudge to the agent to try another tool
                    if not result:
                        content = f"No results found for {function_name}. Please try a broader search or pivot to a different category (e.g., if food search failed, try Instamart for ingredients)."
                    else:
                        content = json.dumps(result)
                    
                    messages.append({
                        "tool_call_id": tool_call.id,
                        "role": "tool",
                        "name": function_name,
                        "content": content
                    })
                else:
                    messages.append({
                        "tool_call_id": tool_call.id,
                        "role": "tool",
                        "name": function_name,
                        "content": "Tool not found"
                    })
        
        return "I'm sorry, I encountered an issue while searching for healthy options."
