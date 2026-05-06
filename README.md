# HealthAMD — NutriAI Assistant

A full-stack AI-agent-driven application that helps users make healthy food choices by integrating with Swiggy MCP tools (Food, Instamart, and Dineout).

## Tech Stack
- **Backend**: FastAPI (Python)
- **AI Agent**: Gemini 2.0 Flash with Function Calling
- **Database**: Supabase (PostgreSQL + RLS)
- **Frontend**: Next.js 14 + Tailwind CSS
- **MCP Layer**: Swiggy MCP Tools (14 Food, 13 Instamart, 8 Dineout)

## Key Features
- **Intelligent Meal Search**: Uses `food_search_restaurants` and `food_get_menu` to find dishes that align with user health goals.
- **Grocery Planning**: Integrated with Swiggy Instamart via `im_search_grocery`.
- **Health Profiles**: Personalized calorie and macro goals stored in Supabase.
- **Habit Tracking**: Automatic logging of food orders for trend analysis.

## Setup
### Backend
1. `cd backend`
2. `pip install -r requirements.txt`
3. Configure `.env` with `GEMINI_API_KEY` and Supabase credentials.
4. `python main.py`

### Frontend
1. `cd frontend`
2. `npm install`
3. `npm run dev`

### Database
Run `supabase/schema.sql` in your Supabase SQL Editor.
