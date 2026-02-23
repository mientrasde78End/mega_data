from pathlib import Path
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 📍 directorio donde está ESTE archivo
BASE_DIR = Path(__file__).resolve().parent

# 📍 core/rag_chat/data/docs.txt
DATA_PATH = BASE_DIR.parent / "data" / "docs.txt"


def load_documents():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"No existe el archivo: {DATA_PATH}")

    loader = TextLoader(str(DATA_PATH), encoding="utf-8")
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    return splitter.split_documents(documents)