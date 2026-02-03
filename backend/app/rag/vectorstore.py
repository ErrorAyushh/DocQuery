import uuid
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

from app.rag.embeddings import get_embedding_model

COLLECTION_NAME = "docquery"


def get_qdrant_client():
    return QdrantClient(url="http://localhost:6333")


def ensure_collection(client, vector_size: int):
    collections = client.get_collections().collections
    names = [c.name for c in collections]

    if COLLECTION_NAME not in names:
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE,
            ),
        )


def index_chunks(chunks):
    model = get_embedding_model()
    client = get_qdrant_client()

    embeddings = model.encode(
        [chunk.page_content for chunk in chunks]
    ).tolist()

    ensure_collection(client, len(embeddings[0]))

    points = [
        PointStruct(
            id=str(uuid.uuid4()),
            vector=vector,
            payload={
                "text": chunk.page_content,
                "page": chunk.metadata.get("page"),
            },
        )
        for chunk, vector in zip(chunks, embeddings)
    ]

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points,
    )
