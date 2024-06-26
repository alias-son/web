from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 필요한 도메인만 허용하도록 변경
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# CSP 설정 미들웨어
class CSPMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self'; connect-src 'self' http://localhost:8000"
        return response

app.add_middleware(CSPMiddleware)

@app.get("/api/data")
def get_data():
    return {"data": "This is data from FastAPI"}
