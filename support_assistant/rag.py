import os
import chromadb
from sentence_transformers import SentenceTransformer

DOCS_PATH = "docs"
COLLECTION_NAME = "zepto_policies"

# Load embedding model
print("Loading embedding model...")
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Create persistent ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")

# Create collection
collection = client.get_or_create_collection(
    name=COLLECTION_NAME,
    metadata={"hnsw:space": "cosine"}
)


def load_documents():
    documents = []

    for filename in sorted(os.listdir(DOCS_PATH)):
        if filename.endswith(".txt"):
            filepath = os.path.join(DOCS_PATH, filename)

            with open(filepath, "r", encoding="utf-8") as file:
                text = file.read().strip()

            documents.append({
                "id": filename,
                "text": text
            })

    return documents


def create_embeddings():
    documents = load_documents()

    ids = []
    texts = []
    embeddings = []

    for doc in documents:
        ids.append(doc["id"])
        texts.append(doc["text"])

        embedding = embedding_model.encode(
            doc["text"]
        ).tolist()

        embeddings.append(embedding)

    collection.upsert(
        ids=ids,
        documents=texts,
        embeddings=embeddings
    )

    print(f"Stored {len(documents)} documents in ChromaDB.")


def retrieve_documents(query, top_k=3):
    query_embedding = embedding_model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results


if __name__ == "__main__":

    print("\nCreating embeddings...")
    create_embeddings()

    print("\nTesting retrieval...")
    
    query = "How much does Zepto charge for delivery?"

    results = retrieve_documents(query, top_k=3)

    print("\nQuery:", query)
    print("\nRetrieved documents:")

    for doc_id, document in zip(
        results["ids"][0],
        results["documents"][0]
    ):
        print("\nID:", doc_id)
        print("Content:", document[:200])
