import random
from typing import List, Dict

class MockSwiggyMCP:
    def __init__(self):
        self.restaurants = [
            {"id": "res_1", "name": "Green Salad Co", "cuisine": "Healthy", "rating": 4.5, "distance": "1.2 km"},
            {"id": "res_2", "name": "Protein Punch", "cuisine": "Continental", "rating": 4.2, "distance": "2.5 km"},
            {"id": "res_3", "name": "Veggie Delight", "cuisine": "North Indian", "rating": 4.0, "distance": "0.8 km"},
        ]
        
        self.menus = {
            "res_1": [
                {"id": "m1", "name": "Quinoa Avocado Salad", "price": 350, "calories": 420, "protein": 12, "is_veg": True},
                {"id": "m2", "name": "Grilled Tofu Bowl", "price": 400, "calories": 380, "protein": 18, "is_veg": True},
            ],
            "res_2": [
                {"id": "m3", "name": "Grilled Chicken Breast", "price": 450, "calories": 520, "protein": 45, "is_veg": False},
                {"id": "m4", "name": "Oatmeal Pancake", "price": 300, "calories": 310, "protein": 10, "is_veg": True},
            ]
        }

    async def search_restaurants(self, query: str, lat: float, lng: float) -> List[Dict]:
        # Simple fuzzy search simulation
        return [r for r in self.restaurants if query.lower() in r["name"].lower() or query.lower() in r["cuisine"].lower()]

    async def get_menu(self, restaurant_id: str) -> List[Dict]:
        return self.menus.get(restaurant_id, [])

    async def search_grocery(self, query: str, lat: float, lng: float) -> List[Dict]:
        items = [
            {"name": "Organic Eggs", "price": 120, "stock": "High"},
            {"name": "Greek Yogurt", "price": 80, "stock": "Medium"},
            {"name": "Avocado", "price": 250, "stock": "Low"},
        ]
        return [i for i in items if query.lower() in i["name"].lower()]
