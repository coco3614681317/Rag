# Rag
rag retrieval-augmented-generation

# RAG 检索增强生成系统 - 基础实践

> 基于向量检索的智能文档问答系统原型



## 项目简介

本项目是一个**RAG (Retrieval-Augmented Generation)** 系统的检索模块实现。通过向量嵌入（Embedding）和相似度检索，能够从非结构化文档中快速找到与用户问题最相关的文本片段。


## 系统架构

    A[用户问题] --> B[嵌入模型<br>mmarco-mMiniLMv2]
    B --> C[向量化查询]
    C --> D[(ChromaDB<br>向量数据库)]
    D --> E[检索Top-K]
    E --> F[重排序<br>（可选）]
    F --> G[返回相关片段]

    ##  致谢 & 参考

本项目参考了 [MarkTechStation](https://github.com/MarkTechStation/VideoCode/tree/main/%E4%BD%BF%E7%94%A8Python%E6%9E%84%E5%BB%BARAG%E7%B3%BB%E7%BB%9F/rag) 
