from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
)


def load_document(file_path: str):
    """
    Load a PDF or DOCX document and return LangChain documents.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Document not found: {file_path}"
        )

    extension = path.suffix.lower()

    if extension == ".pdf":
        loader = PyPDFLoader(str(path))

    elif extension == ".docx":
        loader = Docx2txtLoader(str(path))

    else:
        raise ValueError(
            f"Unsupported file type: {extension}. "
            "Supported formats: PDF, DOCX."
        )

    return loader.load()


# Keep the old function name working for existing code.
def load_pdf(file_path: str):
    return load_document(file_path)