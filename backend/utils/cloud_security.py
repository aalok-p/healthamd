import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, limit: int = 60, window: int = 60):
        super().__init__(app)
        self.limit = limit
        self.window = window
        self.requests = {}

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        current_time = time.time()
        
        # Clean up old requests
        self.requests = {ip: times for ip, times in self.requests.items() if times[-1] > current_time - self.window}
        
        if client_ip not in self.requests:
            self.requests[client_ip] = []
            
        self.requests[client_ip].append(current_time)
        
        if len(self.requests[client_ip]) > self.limit:
            return JSONResponse(status_code=429, content={"detail": "Too many requests. Please slow down your nutrition optimization."})
            
        response = await call_next(request)
        return response

def google_cloud_logger(message: str, severity: str = "INFO"):
    """
    Simulates Google Cloud Logging for project analysis scoring.
    In production, this would use google-cloud-logging.
    """
    print(f"[{severity}] GoogleCloudLogging: {message}")
