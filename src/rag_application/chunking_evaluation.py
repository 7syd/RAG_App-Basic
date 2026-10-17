# # from pathlib import Path

# # from langchain_text_splitters import CharacterTextSplitter
# # from langchain_huggingface import HuggingFaceEmbeddings
# # from langchain_chroma import Chroma

# # from rag_application.loader import load_pdf




# # # -----------------------------
# # # Find project and PDF
# # # -----------------------------

# # project_root = Path(__file__).resolve().parents[2]
# # pdf_path = project_root / "data" / "sample.pdf"

# # documents = load_pdf(str(pdf_path))

# # print(f"Pages loaded: {len(documents)}")


# # # -----------------------------
# # # Combine PDF text
# # # -----------------------------

# # text = "\n".join(doc.page_content for doc in documents)


# # # -----------------------------
# # # Character-based chunking
# # # -----------------------------

# # splitter = CharacterTextSplitter(
# #     separator="",
# #     chunk_size=1000,
# #     chunk_overlap=200
# # )

# # chunks = splitter.split_text(text)

# # print(f"Character chunks: {len(chunks)}")


# # # -----------------------------
# # # Create embeddings
# # # -----------------------------

# # embeddings = HuggingFaceEmbeddings(
# #     model_name="sentence-transformers/all-MiniLM-L6-v2"
# # )


# # # -----------------------------
# # # Store in separate Chroma DB
# # # -----------------------------

# # vectorstore = Chroma.from_texts(
# #     texts=chunks,
# #     embedding=embeddings,
# #     collection_name="character_evaluation",
# #     persist_directory="./chroma_character"
# # )

# # print("Character chunks stored in ChromaDB!")


# # # -----------------------------
# # # Test retrieval
# # # -----------------------------

# # query =  "What are the main deep learning architectures discussed?"

# # results = vectorstore.similarity_search(query, k=3)


# # print("\n========== CHARACTER RETRIEVAL ==========")

# # for i, doc in enumerate(results, start=1):
# #     print(f"\n--- Result {i} ---")
# #     print(doc.page_content)






# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_chroma import Chroma

# from rag_application.loader import load_pdf


# # 1. Load the PDF
# documents = load_pdf("data/sample.pdf")
# text = "\n".join(doc.page_content for doc in documents)

# print(f"Pages loaded: {len(documents)}")


# # 2. Load the embedding model once
# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )


# # 3. Define our test queries
# queries = [
#     "What is this paper about?",
#     "What are the main deep learning architectures discussed?",
#     "What are the main challenges of deep learning?",
# ]


# # 4. Test different chunk sizes
# configurations = [
#     (500, 100),
#     (1000, 200),
#     (1500, 300),
# ]

# for chunk_size, chunk_overlap in configurations:

#     print("\n" + "=" * 65)
#     print(f"CHUNK SIZE: {chunk_size} | OVERLAP: {chunk_overlap}")
#     print("=" * 65)

#     # Split the same text using the current configuration
#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=chunk_size,
#         chunk_overlap=chunk_overlap,
#     )

#     chunks = splitter.split_text(text)

#     print(f"Number of chunks: {len(chunks)}")

#     # Create a fresh in-memory vector store
#     vectorstore = Chroma.from_texts(
#         texts=chunks,
#         embedding=embeddings,
#         collection_name=f"recursive_{chunk_size}",
#     )

#     # Test every query
#     for query in queries:

#         print(f"\nQUERY: {query}")

#         results = vectorstore.similarity_search(query, k=3)

#         for i, doc in enumerate(results, start=1):
#             print(f"\n--- Result {i} ---")
#             print(doc.page_content)

#     # Release this configuration's vector store
#     vectorstore.delete_collection()



# # Diagnostic: find source passages mentioning architectures

# keywords = [
#     "convolutional neural networks",
#     "recurrent neural networks",
#     "transformer",
#     "generative adversarial networks",
#     "U-Net",
#     "long and short term memory",
# ]

# print("\n========== SOURCE CONTENT CHECK ==========")

# for keyword in keywords:
#     matches = []

#     for page_number, document in enumerate(documents, start=1):
#         text_lower = document.page_content.lower()
#         start = 0

#         while True:
#             position = text_lower.find(keyword.lower(), start)

#             if position == -1:
#                 break

#             snippet_start = max(0, position - 180)
#             snippet_end = min(
#                 len(document.page_content),
#                 position + len(keyword) + 300,
#             )

#             matches.append(
#                 (page_number, document.page_content[snippet_start:snippet_end])
#             )

#             start = position + len(keyword)

#     print(f"\nKeyword: {keyword}")
#     print(f"Matches found: {len(matches)}")

#     for page_number, snippet in matches[:2]:
#         print(f"\nPage {page_number}:")
#         print(snippet.replace("\n", " "))



# from langchain_text_splitters import RecursiveCharacterTextSplitter

# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=1000,
#     chunk_overlap=200,
# )

# chunks = splitter.split_text(text)

# print(f"\nTotal recursive chunks: {len(chunks)}")

# keywords = [
#     "3.1. Convolutional",
#     "3.2. Recurrent",
#     "Transformer architecture",
#     "U-Net framework",
# ]

# for keyword in keywords:
#     print(f"\n{'=' * 60}")
#     print(f"SEARCHING FOR: {keyword}")

#     found = False

#     for index, chunk in enumerate(chunks):
#         if keyword.lower() in chunk.lower():
#             found = True
#             print(f"\nChunk index: {index}")
#             print(chunk)
#             break

#     if not found:
#         print("Exact phrase not found in any chunk.")



# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from rag_application.loader import load_pdf

# # Load and combine the PDF text
# documents = load_pdf("data/sample.pdf")
# text = "\n".join(doc.page_content for doc in documents)

# # Split into 1000-character chunks with 200 overlap
# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=1000,
#     chunk_overlap=200,
# )

# chunks = splitter.split_text(text)

# print(f"Pages: {len(documents)}")
# print(f"Recursive chunks: {len(chunks)}")

# # Print chunks containing the detailed architecture sections
# keywords = [
#     "3.1. Convolutional",
#     "3.2. Recurrent",
#     "Transformer architecture",
#     "U-Net framework",
# ]

# for keyword in keywords:
#     print(f"\n{'=' * 60}")
#     print(f"KEYWORD: {keyword}")

#     matches = [
#         (i, chunk)
#         for i, chunk in enumerate(chunks)
#         if keyword.lower() in chunk.lower()
#     ]

#     if not matches:
#         print("No exact phrase found.")
#         continue

#     for index, chunk in matches:
#         print(f"\nCHUNK {index}")
#         print(chunk)



from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

from rag_application.loader import load_pdf
from rag_application.embeddings import create_embeddings
from rag_application.retriever import retrieve_documents


# 1. Load the PDF
documents = load_pdf("data/sample.pdf")

text = "\n".join(
    document.page_content for document in documents
)


# 2. Split the text into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)

chunks = splitter.create_documents([text])

print(f"Total chunks: {len(chunks)}")


# 3. Create embeddings and an in-memory vector store
embeddings = create_embeddings()

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
)


# 4. Ask one question and supply alternate search queries
question = "What are the main deep learning architectures discussed?"

alternate_queries = [
    "Explain convolutional neural networks and their applications.",
    "How do recurrent neural networks and transformers work?",
    "Explain the purpose of U-Net and generative adversarial networks.",
]


# 5. Retrieve and display combined results
results = retrieve_documents(
    vectorstore=vectorstore,
    query=question,
    k=3,
    queries=alternate_queries,
)

print(f"\nOriginal question: {question}")
print(f"Alternate queries: {len(alternate_queries)}")
print(f"Unique chunks retrieved: {len(results)}")

for rank, document in enumerate(results, start=1):
    print(f"\n--- RESULT {rank} ---")
    print(document.page_content[:800])