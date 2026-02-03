from langchain_community.document_loaders import PyPDFLoader


def load_pdf(path: str):
    loader = PyPDFLoader(path)
    documents = loader.load()

    # Normalize page number metadata
    for doc in documents:
        # PyPDFLoader uses 0-based page indexing
        page = doc.metadata.get("page")
        if page is not None:
            doc.metadata["page"] = page + 1  # convert to 1-based
        else:
            doc.metadata["page"] = None

    return documents
