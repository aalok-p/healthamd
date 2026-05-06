from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    supabase_url: str = "https://your-project.supabase.co"
    supabase_anon_key: str = "your-anon-key"
    supabase_service_role_key: str = "your-service-role"
    oxlo_api_key: str = ""
    oxlo_base_url: str = "https://api.oxlo.ai/v1"
    oxlo_model: str = "ministral-14b"
    use_mock_mcp: bool = True
    swiggy_client_id: str = ""
    swiggy_client_secret: str = ""
    secret_key: str = "supersecretkey_change_in_production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 10080
    cors_origins: str = "http://localhost:3000"

    class Config:
        env_file = ".env"
        extra = "ignore"

@lru_cache()
def get_settings() -> Settings:
    return Settings()
