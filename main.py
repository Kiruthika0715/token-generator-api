from __future__ import annotations

import hashlib
import re
from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Token Generator API", version="1.0.0")

BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_DIR = BASE_DIR / "templates"
INDEX_HTML = TEMPLATE_DIR / "index.html"


class TextRequest(BaseModel):
    text: str = Field(..., description="The text to tokenize")


class TokenResponse(BaseModel):
    text: str
    tokens: list[str]
    checksum: str


def generate(text: str) -> list[str]:
    """Split text into tokens using whitespace as a delimiter."""
    if not text:
        return []
    return re.findall(r"\S+", text)


@app.get("/")
async def read_root() -> str:
    """Serve the interactive HTML form for the user."""
    return INDEX_HTML.read_text(encoding="utf-8")


@app.post("/generate", response_model=TokenResponse)
async def generate_route(payload: TextRequest) -> TokenResponse:
    """Accept text and return tokenized output plus a checksum."""
    tokens = generate(payload.text)
    checksum = hashlib.sha256(payload.text.encode("utf-8")).hexdigest()
    return TokenResponse(text=payload.text, tokens=tokens, checksum=checksum)


@app.post("/api/tokenize", response_model=TokenResponse)
async def tokenize_route(payload: TextRequest) -> TokenResponse:
    """Alias endpoint that tokenizes text and returns the result."""
    return await generate_route(payload)
