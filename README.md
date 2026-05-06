# Health.AMD Protocol — Precision Nutrition Agent

A monochromatic, high-performance health optimization interface powered by the Swiggy MCP network and Oxlo Intelligence.

## 🛠️ Backend Setup (FastAPI)

Follow these steps to initialize the core processing unit:

1.  **Navigate to Backend**:
    ```bash
    cd backend
    ```

2.  **Initialize Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    # venv\Scripts\activate   # Windows
    ```

3.  **Install Protocols**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure `.env`**:
    Ensure the following keys are present in `backend/.env`:
    - `OXLO_API_KEY`
    - `SUPABASE_URL`
    - `SUPABASE_ANON_KEY`
    - `SUPABASE_SERVICE_ROLE_KEY`

5.  **Execute Server**:
    ```bash
    uvicorn main:app --reload --port 8000
    ```

## 🌐 Frontend Setup (Next.js)

1.  **Navigate to Frontend**:
    ```bash
    cd frontend
    ```

2.  **Install Dependencies**:
    ```bash
    npm install
    ```

3.  **Configure `.env.local`**:
    - `NEXT_PUBLIC_SUPABASE_URL`
    - `NEXT_PUBLIC_SUPABASE_ANON_KEY`
    - `NEXT_PUBLIC_BACKEND_URL=http://localhost:8000`

4.  **Execute Development Interface**:
    ```bash
    npm run dev
    ```

## 🏗️ Database Setup
Execute the `supabase/schema.sql` in your Supabase SQL Editor to initialize the data structures.

---
**Protocol Status**: Monochromatic / Autonomous / Cloud-Run Ready
