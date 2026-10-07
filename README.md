# RAG Application

A beginner-friendly Retrieval-Augmented Generation (RAG) application built with Python and LangChain.

The project is being developed step by step to understand how PDF documents can be loaded, chunked, converted into embeddings, stored in a vector database, and retrieved using semantic similarity.

## Project Goal

The main goal is to build a RAG pipeline that can:

1. Load information from PDF documents
2. Split the document into smaller chunks
3. Generate embeddings for the chunks
4. Store the embeddings in a vector database
5. Retrieve relevant chunks based on a user query
6. Eventually use an LLM to generate an answer from the retrieved information

## Current Architecture

```text
PDF
 ↓
PyPDFLoader
 ↓
Document Pages
 ↓
Text Chunking
 ↓
Hugging Face Embeddings
 ↓
ChromaDB
 ↓
Similarity Search
 ↓
Retrieved Context
 ↓
LLM (Future)
 ↓
Final Answer
```

## Technologies Used

- Python
- LangChain
- PyPDF
- Hugging Face Sentence Transformers
- ChromaDB
- uv
- FAISS (planned)

## Embedding Model

The current prototype uses:

`sentence-transformers/all-MiniLM-L6-v2`

This is a lightweight sentence-transformer model that produces **384-dimensional embeddings**.

The model is currently being used locally for experimentation.

## PDF Processing

PDF files are loaded using LangChain's `PyPDFLoader`.

Example test document:

```text
data/
└── sample.pdf
```

The current test PDF contains 7 pages.

## Chunking

The project is currently evaluating different chunking strategies.

Current methods being tested:

- Character-based chunking
- Recursive Character chunking
- Token-based chunking
- Other methods will be evaluated later

The current Recursive Character Splitter configuration is:

```python
chunk_size = 1000
chunk_overlap = 200
```

The goal is to select the chunking strategy that provides the best retrieval quality rather than simply choosing the method that produces the most or fewest chunks.

## Vector Database

ChromaDB is currently being used for storing embeddings and performing similarity search.

The prototype uses the retrieved chunks as context for answering questions about the source document.

FAISS will be evaluated later as an alternative vector search solution.

## Project Structure

```text
RAG application/
│
├── data/
│   └── sample.pdf
│
├── src/
│   └── rag_application/
│       ├── __init__.py
│       ├── loader.py
│       ├── chunker.py
│       ├── embeddings.py
│       ├── vectorstore.py
│       ├── retriever.py
│       ├── chunking_comparison.py
│       └── chunking_evaluation.py
│
├── .venv/
├── main.py
├── pyproject.toml
├── uv.lock
└── README.md
```

## Running the Project

Create the environment and install dependencies using `uv`.

Run the main RAG pipeline:

```bash
uv run python main.py
```

Run the chunking comparison:

```bash
uv run python src/rag_application/chunking_comparison.py
```

Run the chunking evaluation:

```bash
uv run python src/rag_application/chunking_evaluation.py
```

## Current Status

### Completed

- [x] Python/uv environment setup
- [x] PDF loading
- [x] PDF text extraction
- [x] Recursive character chunking
- [x] Character-based chunking experiment
- [x] Hugging Face embeddings
- [x] ChromaDB vector storage
- [x] Basic similarity retrieval
- [x] Initial chunking comparison

### In Progress

- [ ] Compare retrieval quality between chunking methods
- [ ] Select the best chunking strategy
- [ ] Evaluate hybrid chunking if necessary
- [ ] Improve retrieval
- [ ] Add FAISS
- [ ] Add an LLM
- [ ] Build the complete RAG pipeline
- [ ] Test with multiple PDF documents

## Example Query

The current prototype uses questions such as:

```text
What is this document about?
```

The system converts the query into an embedding and searches ChromaDB for the most semantically similar document chunks.

## Future Improvements

The project will eventually explore:

- Better chunking strategies
- Hybrid chunking
- FAISS vs ChromaDB
- Metadata filtering
- Retrieval evaluation
- LLM-based answer generation
- Multiple PDF support
- `.env` configuration
- Improved error handling
- A simple user interface

## Learning Objective

This project is being developed incrementally to understand the individual components of a RAG system rather than treating RAG as a single black-box implementation.
