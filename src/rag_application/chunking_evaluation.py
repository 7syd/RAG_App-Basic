from pathlib import Path

from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from rag_application.loader import load_pdf


# -----------------------------
# Find project and PDF
# -----------------------------

project_root = Path(__file__).resolve().parents[2]
pdf_path = project_root / "data" / "sample.pdf"

documents = load_pdf(str(pdf_path))

print(f"Pages loaded: {len(documents)}")


# -----------------------------
# Combine PDF text
# -----------------------------

text = "\n".join(doc.page_content for doc in documents)


# -----------------------------
# Character-based chunking
# -----------------------------

splitter = CharacterTextSplitter(
    separator="",
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_text(text)

print(f"Character chunks: {len(chunks)}")


# -----------------------------
# Create embeddings
# -----------------------------

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# -----------------------------
# Store in separate Chroma DB
# -----------------------------

vectorstore = Chroma.from_texts(
    texts=chunks,
    embedding=embeddings,
    persist_directory="./chroma_character"
)

print("Character chunks stored in ChromaDB!")


# -----------------------------
# Test retrieval
# -----------------------------

query = "What is this paper about?"

results = vectorstore.similarity_search(query, k=3)


print("\n========== CHARACTER RETRIEVAL ==========")

for i, doc in enumerate(results, start=1):
    print(f"\n--- Result {i} ---")
    print(doc.page_content)