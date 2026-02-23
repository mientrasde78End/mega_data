# core/asgi.py
import os
from django.core.asgi import get_asgi_application
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

# Django ASGI app
django_asgi_app = get_asgi_application()  # ya es ASGI

# FastAPI app
from .rag_chat.rag.chain import get_rag_chain  # import relativo dentro de core

fastapi_app = FastAPI(title="RAG Chat API")

fastapi_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # frontend domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# RAG global
rag_chain = None

class Question(BaseModel):
    question: str

@fastapi_app.get("/")
async def health():
    return {"status": "ok"}

@fastapi_app.post("/chat")
async def chat(data: Question):
    global rag_chain
    if rag_chain is None:
        rag_chain = get_rag_chain()
    result = rag_chain.invoke(data.question)
    return {"answer": result}

# ---------------------------
# Montaje final con Starlette
# ---------------------------
from starlette.routing import Mount
from starlette.applications import Starlette

application = Starlette(
    routes=[
        Mount("/api/rag", app=fastapi_app),    # FastAPI en /api/rag
        Mount("/", app=django_asgi_app),       # Django ASGI normal
    ]
)