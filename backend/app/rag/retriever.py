from qdrant_client import QdrantClient
from app.rag.embeddings import get_embedding_model

COLLECTION_NAME = "docquery"


def retrieve_chunks(query: str, top_k: int = 4):
    client = QdrantClient(url="http://localhost:6333")
    model = get_embedding_model()

    query_vector = model.encode(query).tolist()

    search_results = client.query_points(
        collection_name=COLLECTION_NAME,
        prefetch=[],
        query=query_vector,
        limit=top_k,
    )

    return [
    {
        "text": point.payload["text"],
        "page": point.payload.get("page"),
    }
    for point in search_results.points
]

