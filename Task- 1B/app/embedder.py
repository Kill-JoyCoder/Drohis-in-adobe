from sentence_transformers import SentenceTransformer
import numpy as np
import os

_model = None

def get_model():
    global _model
    if _model is None:
        local_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../models/all-MiniLM-L6-v2-local"))
        _model = SentenceTransformer(local_path)
    return _model

def get_embeddings(texts):
    model = get_model()
    return model.encode(texts, convert_to_numpy=True, normalize_embeddings=True)

def get_task_embedding(persona, job):
    model = get_model()
    return model.encode(f"{persona}: {job}", convert_to_numpy=True, normalize_embeddings=True)
