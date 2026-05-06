-- Enable RLS
-- Users table is handled by Supabase Auth

-- User Profiles
CREATE TABLE public.profiles (
    id UUID REFERENCES auth.users ON DELETE CASCADE PRIMARY KEY,
    full_name TEXT,
    calorie_goal INTEGER DEFAULT 2000,
    protein_goal INTEGER DEFAULT 150,
    carbs_goal INTEGER DEFAULT 200,
    fat_goal INTEGER DEFAULT 60,
    allergies TEXT[] DEFAULT '{}',
    dietary_preferences TEXT[] DEFAULT '{}',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Order History (tracked for habits)
CREATE TABLE public.orders (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    user_id UUID REFERENCES auth.users ON DELETE CASCADE,
    items JSONB,
    total_amount DECIMAL,
    restaurant_name TEXT,
    calories_estimated INTEGER,
    health_score INTEGER,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Habit Streaks
CREATE TABLE public.habits (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    user_id UUID REFERENCES auth.users ON DELETE CASCADE,
    date DATE DEFAULT CURRENT_DATE,
    calories_consumed INTEGER DEFAULT 0,
    is_healthy_day BOOLEAN DEFAULT FALSE,
    UNIQUE(user_id, date)
);

-- RLS Policies
ALTER TABLE public.profiles ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Users can view own profile" ON public.profiles FOR SELECT USING (auth.uid() = id);
CREATE POLICY "Users can update own profile" ON public.profiles FOR UPDATE USING (auth.uid() = id);

ALTER TABLE public.orders ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Users can view own orders" ON public.orders FOR SELECT USING (auth.uid() = user_id);

ALTER TABLE public.habits ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Users can view own habits" ON public.habits FOR SELECT USING (auth.uid() = user_id);
