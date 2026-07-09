

# 1. 3D RAG System Architecture

A 3D object retrieval system based on the Objaverse dataset.

## Modules

| Module | Description |
|--------|-------------|
| **database** | 3D model database (Objaverse) |
| **query** | User input (text or 3D model) |
| **GLB Model** | 3D model file format |
| **Mesh Process** | Mesh preprocessing (Open3D/Trimesh) |
| **PointCloud** | Point cloud conversion & sampling |
| **Feature** | Feature extraction & vectorization |
| **Cosine Similarity** | Similarity computation |
| **Top-K** | Return top K most similar results |

## Tech Stack

| Component | Technology |
|-----------|------------|
| 3D Processing | Open3D, Trimesh |
| Feature Extraction | PointNet / Transformer |
| Vector Database | ChromaDB |
| Text Encoding | Sentence-Transformers |
| Deep Learning | PyTorch |

## Data Flow

1. **Database Side**: Objaverse GLB → Mesh → PointCloud → Feature → Vector Store
2. **Query Side**: Input (text/3D model) → Feature → Vector Search
3. **Matching**: Cosine Similarity → Top-K Results



# 2. RAG Retrieval-Augmented Generation System - Basic Practice

> A prototype of an intelligent document Q&A system based on vector retrieval
Rag_textt project is a **retrieval module implementation** of a RAG (Retrieval-Augmented Generation) system. Through vector embeddings and similarity search, it can quickly retrieve the most relevant text segments from unstructured documents in response to user queries.


Reference [MarkTechStation](https://github.com/MarkTechStation/VideoCode/tree/main/%E4%BD%BF%E7%94%A8Python%E6%9E%84%E5%BB%BARAG%E7%B3%BB%E7%BB%9F/rag) 
