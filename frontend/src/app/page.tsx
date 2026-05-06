"use client";

import { useState } from "react";
import { supabase } from "@/lib/supabase";

export default function Home() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const handleChat = async () => {
    setLoading(true);
    try {
      // Mock user_id for demo
      const userId = "00000000-0000-0000-0000-000000000000";
      const backendUrl = process.env.NEXT_PUBLIC_BACKEND_URL || "http://localhost:8000";
      const res = await fetch(`${backendUrl}/chat?user_id=${userId}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: query }),
      });
      const data = await res.json();
      setResponse(data.response);
    } catch (error) {
      console.error(error);
      setResponse("Error connecting to NutriAI Agent.");
    }
    setLoading(false);
  };

  return (
    <main className="min-h-screen bg-slate-950 text-white p-8">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-5xl font-extrabold bg-gradient-to-r from-emerald-400 to-cyan-400 bg-clip-text text-transparent mb-8">
          NutriAI Assistant
        </h1>
        
        <div className="bg-slate-900/50 backdrop-blur-xl border border-slate-800 rounded-3xl p-6 mb-8">
          <div className="flex gap-4">
            <input
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="I'm looking for a high-protein vegetarian dinner under 500 calories..."
              className="flex-1 bg-slate-800/50 border border-slate-700 rounded-2xl px-6 py-4 focus:outline-none focus:ring-2 focus:ring-emerald-500 transition-all"
            />
            <button
              onClick={handleChat}
              disabled={loading}
              className="bg-emerald-500 hover:bg-emerald-600 px-8 py-4 rounded-2xl font-bold transition-all disabled:opacity-50"
            >
              {loading ? "Thinking..." : "Ask Agent"}
            </button>
          </div>
        </div>

        {response && (
          <div className="bg-slate-900/50 backdrop-blur-xl border border-slate-800 rounded-3xl p-8 animate-in fade-in slide-in-from-bottom-4">
            <h2 className="text-emerald-400 font-bold mb-4">NutriAI Response:</h2>
            <p className="text-slate-300 leading-relaxed text-lg whitespace-pre-wrap">
              {response}
            </p>
          </div>
        )}
      </div>
    </main>
  );
}
