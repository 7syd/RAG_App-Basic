from pathlib import Path

from langchain_text_splitters import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
    SentenceTransformersTokenTextSplitter,
)

from rag_application.loader import load_pdf


project_root = Path(__file__).resolve().parents[2]
pdf_path = project_root / "data" / "sample.pdf"

print("Project root:", project_root)
print("PDF path:", pdf_path)
print("PDF exists:", pdf_path.exists())

documents = load_pdf(str(pdf_path))

text = "\n".join(doc.page_content for doc in documents)