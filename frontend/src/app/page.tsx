"use client";

import { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Send, Zap, Activity, Target, ShieldCheck, ChefHat } from "lucide-react";
import Image from "next/image";

export default function Home() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => setScrolled(window.scrollY > 50);
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  const handleChat = async () => {
    if (!query.trim()) return;
    setLoading(true);
    setResponse("");
    try {
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
      setResponse("System error: Unable to reach processing unit. Ensure backend is active.");
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-black text-white selection:bg-white selection:text-black overflow-x-hidden font-sans">
      {/* Navigation */}
      <nav className={`fixed top-0 w-full z-50 transition-all duration-300 ${scrolled ? "bg-black/90 backdrop-blur-md border-b border-white/10 py-4" : "bg-transparent py-6"}`}>
        <div className="max-w-7xl mx-auto px-6 flex justify-between items-center">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 bg-white rounded-sm flex items-center justify-center">
              <Zap className="text-black w-5 h-5 fill-current" />
            </div>
            <span className="text-lg font-bold tracking-tighter uppercase">Health.AMD</span>
          </div>
          <div className="hidden md:flex items-center gap-8 text-[10px] font-bold uppercase tracking-[0.2em] text-white/50">
            <a href="#" className="hover:text-white transition-colors">Interface</a>
            <a href="#" className="hover:text-white transition-colors">Protocol</a>
            <a href="#" className="hover:text-white transition-colors">Database</a>
            <button className="bg-white text-black px-6 py-2 rounded-sm hover:bg-gray-200 transition-all duration-300">
              Access
            </button>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="relative pt-40 pb-20 px-6">
        <div className="max-w-7xl mx-auto grid lg:grid-cols-2 gap-16 items-center">
          <motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
          >
            <h1 className="text-7xl lg:text-8xl font-bold leading-[0.9] mb-10 tracking-tighter uppercase">
              Precision <br />
              Nutrition.
            </h1>
            <p className="text-lg text-white/60 mb-12 leading-relaxed max-w-md font-medium">
              Autonomous agent for health optimization. Real-time analysis and procurement. 
            </p>
            
            <div className="flex flex-wrap gap-6 mb-12 border-l border-white/40 pl-6">
              <div className="flex flex-col gap-1">
                <span className="text-[10px] uppercase tracking-widest text-white/50">Target</span>
                <span className="text-sm font-bold uppercase">Macro Precision</span>
              </div>
              <div className="flex flex-col gap-1">
                <span className="text-[10px] uppercase tracking-widest text-white/50">Status</span>
                <span className="text-sm font-bold uppercase">Ready</span>
              </div>
            </div>
          </motion.div>

          <motion.div 
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 1.5, delay: 0.2 }}
            className="relative"
          >
            <div className="relative aspect-square grayscale contrast-125 brightness-100 rounded-sm overflow-hidden border border-white/20 group">
              <Image 
                src="/hero.png" 
                alt="Health Interface" 
                fill
                className="object-cover transition-transform duration-1000 group-hover:scale-105"
              />
              <div className="absolute inset-0 bg-black/20 mix-blend-overlay"></div>
            </div>
          </motion.div>
        </div>
      </section>

      {/* AI Assistant Section */}
      <section className="py-20 px-6 relative">
        <div className="max-w-5xl mx-auto relative">
          <div className="flex items-center gap-4 mb-12">
            <div className="h-[1px] flex-1 bg-white/20"></div>
            <h2 className="text-[10px] font-bold uppercase tracking-[0.4em] text-white/60">Command Interface</h2>
            <div className="h-[1px] flex-1 bg-white/20"></div>
          </div>

          <div className="relative bg-white/[0.05] border border-white/20 p-2 rounded-sm focus-within:border-white/60 transition-colors">
            <div className="flex items-center gap-4">
              <input
                type="text"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                onKeyDown={(e) => e.key === "Enter" && handleChat()}
                placeholder="INPUT COMMAND..."
                className="flex-1 bg-transparent border-none outline-none text-xl text-white placeholder:text-white/20 px-6 py-4 uppercase font-bold tracking-tight"
              />
              <button
                onClick={handleChat}
                disabled={loading}
                className="bg-white text-black px-10 py-4 font-bold uppercase text-xs tracking-widest hover:bg-gray-200 transition-all disabled:opacity-50"
              >
                {loading ? "EXECUTING..." : "EXECUTE"}
              </button>
            </div>
          </div>

          <AnimatePresence mode="wait">
            {response && !loading && (
              <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                className="mt-12 border border-white/20 bg-white/[0.02]"
              >
                <div className="border-b border-white/20 px-8 py-3 flex items-center justify-between">
                  <span className="text-[10px] font-bold uppercase tracking-widest text-white/60">Response Data</span>
                  <div className="flex gap-1">
                    <div className="w-1.5 h-1.5 bg-white/60"></div>
                    <div className="w-1.5 h-1.5 bg-white/60"></div>
                  </div>
                </div>
                <div className="p-12">
                  <p className="text-white text-xl leading-relaxed font-light tracking-tight whitespace-pre-wrap">
                    {response}
                  </p>
                </div>
              </motion.div>
            )}
          </AnimatePresence>

          {/* Minimal Suggestions */}
          <div className="mt-12 grid grid-cols-2 md:grid-cols-4 gap-4">
            {[
              "HIGH PROTEIN",
              "LOW CALORIE",
              "VEGETARIAN",
              "RECOVERY"
            ].map((chip) => (
              <button
                key={chip}
                onClick={() => setQuery(chip)}
                className="py-4 border border-white/10 text-[10px] font-bold tracking-[0.2em] text-white/50 hover:border-white/60 hover:text-white transition-all uppercase bg-white/[0.02]"
              >
                {chip}
              </button>
            ))}
          </div>
        </div>
      </section>
    </div>
  );
}
