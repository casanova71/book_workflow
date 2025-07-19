# chromadb/chroma_ops.py

import chromadb
from chromadb.utils.embedding_functions import DefaultEmbeddingFunction

class VersionManager:
    def __init__(self):
        self.client = chromadb.PersistentClient(path=".chroma_store")
        self.collection_name = "book_versions"

        embedding_fn = DefaultEmbeddingFunction()
        
        if self.collection_name not in [col.name for col in self.client.list_collections()]:
            self.collection = self.client.create_collection(name=self.collection_name, embedding_function=embedding_fn)
        else:
            self.collection = self.client.get_collection(name=self.collection_name, embedding_function=embedding_fn)

    def add_version(self, original_text, rewritten_text, reward_score):
        version_id = f"version_{len(self.collection.get()['ids']) + 1}"
        metadata = {
            "original": original_text,
            "rewritten": rewritten_text,
            "score": reward_score
        }
        self.collection.add(
            documents=[rewritten_text],
            ids=[version_id],
            metadatas=[metadata]
        )

    def fetch_latest(self):
        all_docs = self.collection.get()
        if not all_docs['documents']:
            return None
        last_index = len(all_docs['documents']) - 1
        return {
            "text": all_docs['documents'][last_index],
            "score": all_docs['metadatas'][last_index]['score'],
            "original": all_docs['metadatas'][last_index]['original']
        }

def get_latest_version():
    return VersionManager()
