import os
from typing import List, Optional
from pydantic import BaseModel, Field

# --- Food MCP Tools ---

class SearchRestaurants(BaseModel):
    query: str = Field(..., description="Cuisine, restaurant name, or dish type")
    lat: float
    lng: float

class GetMenu(BaseModel):
    restaurant_id: str

class PlaceOrder(BaseModel):
    restaurant_id: str
    items: List[dict]
    delivery_address: str

# --- Instamart MCP Tools ---

class SearchGrocery(BaseModel):
    query: str = Field(..., description="Item name (e.g., 'organic eggs', 'avocado')")
    lat: float
    lng: float

# --- Dineout MCP Tools ---

class BookTable(BaseModel):
    restaurant_id: str
    party_size: int
    booking_time: str

# --- Tool Definitions for Gemini ---

tools = [
    {
        "function_declarations": [
            {
                "name": "food_search_restaurants",
                "description": "Search for restaurants nearby on Swiggy Food",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "Cuisine or restaurant name"},
                        "lat": {"type": "number"},
                        "lng": {"type": "number"}
                    },
                    "required": ["query", "lat", "lng"]
                }
            },
            {
                "name": "food_get_menu",
                "description": "Get the full menu of a specific restaurant",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "restaurant_id": {"type": "string"}
                    },
                    "required": ["restaurant_id"]
                }
            },
            {
                "name": "im_search_grocery",
                "description": "Search for groceries on Swiggy Instamart",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string"},
                        "lat": {"type": "number"},
                        "lng": {"type": "number"}
                    },
                    "required": ["query", "lat", "lng"]
                }
            }
        ]
    }
]
