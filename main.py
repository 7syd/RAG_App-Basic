from pathlib import Path

from rag_application.loader import load_document
from rag_application.chunker import split_documents
from rag_application.embeddings import create_embeddings
from rag_application.vectorstore import create_vectorstore
from rag_application.retriever import retrieve_documents


def main():
    file_path = "data/sample.pdf"

    # 1. Load the document
    print(f"Loading: {file_path}")
    documents = load_document(file_path)
    print(f"Extracted pages/sections: {len(documents)}")

    # 2. Split the extracted text into chunks
    chunks = split_documents(documents)
    print(f"Created chunks: {len(chunks)}")

    # 3. Generate embeddings
    print("Loading embedding model...")
    embeddings = create_embeddings()

    # 4. Create the vector store
    print("Creating vector store...")
    vectorstore = create_vectorstore(chunks, embeddings)

    # 5. Accept questions interactively
    print("\nRAG retrieval is ready.")
    print("Ask questions about your document, or type 'exit' to quit.")

    while True:
        question = input("\nYour question: ").strip()

        if question.lower() in {"exit", "quit"}:
            break

        if not question:
            continue

        results = retrieve_documents(
            vectorstore=vectorstore,
            query=question,
            k=3,
        )

        if not results:
            print("No relevant information found.")
            continue

        for index, result in enumerate(results, start=1):
            print(
                f"\n--- Chunk {index} | "
                f"Distance: {result['distance']:.4f} ---"
            )
            print(result["document"].page_content[:800])
if __name__ == "__main__":
    main()