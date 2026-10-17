from rag_application.loader import load_document

files = [
    "data/sample.pdf",
    # Add a DOCX file here when you have one.
    # "data/sample.docx",
]

for file_path in files:
    documents = load_document(file_path)

    print(f"\nFile: {file_path}")
    print(f"Extracted sections/pages: {len(documents)}")
    print(f"Preview: {documents[0].page_content[:300]}")