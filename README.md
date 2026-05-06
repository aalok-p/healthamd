# Health.AMD

> **Protocol for Precision Nutrition & Autonomous Procurement.**

Health.AMD is a high-performance agentic interface that leverages the **Swiggy MCP** ecosystem and **Oxlo Intelligence** to bridge the gap between nutritional goals and actual food consumption. It doesn't just track; it analyzes, recommends, and facilitates.

---

## 🏗️ Architecture

- **Core**: FastAPI (Python 3.12+)
- **Intelligence**: Oxlo (Ministral-14b via OpenAI client)
- **Database**: Supabase (PostgreSQL + RLS)
- **Interface**: Next.js 14 + Tailwind CSS (Monochromatic / Minimal)
- **Tooling**: Swiggy MCP (Food, Instamart, Dineout)

---

## 🚀 Quick Start

### 1. Backend Engine
```bash
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### 2. Frontend Interface
```bash
cd frontend
npm install
npm run dev
```

### 3. Database Migration
Execute `supabase/schema.sql` in your Supabase SQL Editor.

---

## 🔑 Environment Configuration

### Backend (`backend/.env`)
- `OXLO_API_KEY`: Intelligence access key.
- `OXLO_BASE_URL`: `https://api.oxlo.ai/v1`
- `SUPABASE_URL` / `SUPABASE_ANON_KEY`: Database connectivity.

### Frontend (`frontend/.env.local`)
- `NEXT_PUBLIC_SUPABASE_URL`
- `NEXT_PUBLIC_SUPABASE_ANON_KEY`
- `NEXT_PUBLIC_BACKEND_URL`: `http://localhost:8000`

---

## 📦 Deployment
The project is **Cloud Run Ready**.
- Backend: `backend/Dockerfile`
- Frontend: `frontend/Dockerfile`

---
**Health.AMD** — *Monochromatic / Autonomous / Precision.*
