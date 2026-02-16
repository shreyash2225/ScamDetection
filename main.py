from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import os

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API model
class TextInput(BaseModel):
    text: str

# API endpoint
@app.post("/api/check")
def check_scam(data: TextInput):
    text = data.text.lower()

    if "otp" in text or "urgent" in text or "click" in text:
        return {"result": "Scam", "confidence": 100}
    else:
        return {"result": "Safe", "confidence": 100}

# Serve frontend
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "frontend")), name="static")
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "frontend"))

@app.get("/", response_class=HTMLResponse)
def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

