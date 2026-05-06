# Health.AMD: Technical Implementation & Protocol

Health.AMD is an agentic nutrition assistant designed to bridge the gap between high-level health goals and real-world food procurement. It utilizes a sophisticated tool-calling loop integrated with the Swiggy MCP (Model Context Protocol) ecosystem.

---

## Technical Approach

### 1. Agentic Orchestration Layer
The core of the system is a multi-turn reasoning loop powered by the Oxlo Intelligence engine (Ministral-14b). Unlike simple chat interfaces, Health.AMD implements a manual tool-calling cycle:
- **Reasoning Phase**: The agent analyzes the user's intent (e.g., "Find high-protein dinner") against their Supabase profile (allergies, macro goals).
- **Action Phase**: The agent generates specific tool calls based on the Swiggy MCP schema (e.g., `food_search_restaurants`).
- **Observation Phase**: The system executes these calls against a mock or live Swiggy client and returns the raw data to the agent.
- **Synthesis Phase**: The agent processes the results to provide a health-scored recommendation.

### 2. Tool Mapping & MCP Integration
The protocol maps 35 distinct tools across three Swiggy domains:
- **Food**: Restaurant discovery, menu analysis, and order placement.
- **Instamart**: Grocery search and availability tracking.
- **Dineout**: Table reservation for goal-aligned dining.

Each tool is defined using OpenAI-compatible function schemas, ensuring seamless integration with the Ministral-14b model.

### 3. Data Persistence (Supabase)
Persistency is handled via a PostgreSQL backend on Supabase with Row Level Security (RLS) to ensure data isolation:
- **User Profiles**: Stores granular health data including calorie targets and allergen lists.
- **Habit Engine**: Logs orders to track streaks and nutritional trends over time.

---

## Infrastructure

### Backend (FastAPI)
A modular Python 3.12 architecture focused on performance and scalability.
- **Location**: `backend/`
- **Execution**: `uvicorn main:app --port 8000`
- **Dependencies**: Fixed versioning to resolve `httpx` and `supabase-py` conflicts.

### Frontend (Next.js)
A high-contrast, monochromatic interface built for speed and clarity.
- **Location**: `frontend/`
- **Execution**: `npm run dev`
- **Styling**: Tailwind CSS with custom glassmorphism and Framer Motion for protocol-level animations.

---

## Environment Configuration

### Backend Connectivity
- `OXLO_API_KEY`: Intelligence endpoint access.
- `OXLO_BASE_URL`: https://api.oxlo.ai/v1
- `OXLO_MODEL`: ministral-14b
- `SUPABASE_URL`: PostgreSQL connection endpoint.
- `USE_MOCK_MCP`: Set to true for local development without live Swiggy credentials.

### Frontend Connectivity
- `NEXT_PUBLIC_BACKEND_URL`: Points to the FastAPI service (default: http://localhost:8000).
- `NEXT_PUBLIC_SUPABASE_URL`: Public database endpoint.

---

## Deployment Strategy
The system is containerized for Google Cloud Run compatibility:
- **Backend**: Multi-stage Python build listening on dynamic port environment variables.
- **Frontend**: Optimized Node.js runner for static assets and server-side logic.

Health.AMD Protocol — Monochromatic / Autonomous / Precision.
