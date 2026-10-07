from rag_application.loader import load_pdf
from rag_application.chunker import split_documents
from rag_application.embeddings import create_embeddings
from rag_application.vectorstore import create_vectorstore
from rag_application.retriever import retrieve_documents



documents = load_pdf("data/sample.pdf")

chunks = split_documents(documents)

embeddings = create_embeddings()

vector = embeddings.embed_query("What is this Document about ?")

vectorstore = create_vectorstore(chunks, embeddings)

print(f"Embedding dimensions: {len(vector)}")
print(f"First 10 Values : {vector[:10]}")
print(f"Number of pages : {len(documents)}")
print(f"Number of chunks : {len(chunks)}")
print("Documents Successfully stored in ChromaDB!")

print('\n----- First Chunk ------')
print(chunks[0].page_content)

print("\n ----- Metadata -----")
print(chunks[0].metadata)


query = "What is this document about?"

results = retrieve_documents(vectorstore, query)

print("\n--- Retrieved Chunks ---")

for i, doc in enumerate(results, start=1):
    print(f"\n--- Result {i} ---")
    print(doc.page_content)
    print(f"Metadata: {doc.metadata}")







# Test statement ✅
# print(f"Number of pages : {len(documents)}")
# print(documents[0])