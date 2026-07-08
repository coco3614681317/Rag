#powershell进入rag文件夹   D:  cd rag
#uv run --with jupyter jupyter lab


#RAG 
#1.分片

from typing import List

def split_into_chunks(doc_file: str) -> List [str]:  #创建函数 分片段chunk,参数为doc_file
    with open(doc_file, 'r')as file:
        content = file.read()                        #读取文件内容，放在content变量里面
    return [chunk for chunk in content.split("\n\n")]  #把content切分为多个chunk

chunks = split_into_chunks("doc.md")    #排序

for i, chunk in enumerate(chunks):    # 循环遍历拿到所有的片段， 把片段编号和对应内容都打印出来
    print(f"[{i}] {chunk}\n")


from typing import List

def split_into_chunks(doc_file: str) -> List [str]:
    with open(doc_file, 'r',encoding='utf-8')as file:
        content = file.read()
    return [chunk for chunk in content.split("\n\n")]

chunks = split_into_chunks("doc.md")

for i, chunk in enumerate(chunks):
    print(f"[{i}] {chunk}\n")


#2. 索引
from sentence_transformers import SentenceTransformer # 引入对象

embedding_model = SentenceTransformer("shibing624/text2vec-base-chinese")  #加载模型


import os

# 1. 先设置镜像源环境变量
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

# 2. 强制修改 huggingface_hub 的全局配置（彻底锁死镜像）
from huggingface_hub import constants
constants.ENDPOINT = 'https://hf-mirror.com'

# 3. 清除可能干扰的代理设置（确保不走代理）
os.environ.pop('HTTP_PROXY', None)
os.environ.pop('HTTPS_PROXY', None)

print(f"🔍 当前HF_ENDPOINT: {os.environ.get('HF_ENDPOINT')}")

from sentence_transformers import SentenceTransformer
from typing import List

print("🚀 开始从镜像源下载模型（强制配置）...")
embedding_model = SentenceTransformer("shibing624/text2vec-base-chinese")
print("✅ 模型加载完成！")

def embed_chunk(chunk: str) -> List[float]:
    embedding = embedding_model.encode(chunk)
    return embedding.tolist()

test_embedding = embed_chunk("测试内容")
print(f"向量维度: {len(test_embedding)}")
print(test_embedding)



#3. 存入向量数据库

import chromadb
from typing import List

chromadb_client = chromadb.EphemeralClient()
chromadb_collection = chromadb_client.get_or_create_collection(name="default")

def save_embeddings(chunks: List[str], embeddings: List[List[float]]) -> None:
    ids = [str(i) for i in range(len(chunks))]
    chromadb_collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids
    )
    print(f"✅ 成功添加 {len(chunks)} 条数据")

# ⭐ 关键：教程跳过的这一步，你要补上！
embeddings = [embed_chunk(chunk) for chunk in chunks]  # 👈 生成向量

# 现在 embeddings 有值了，可以存入
save_embeddings(chunks, embeddings)

#4. 召回
def retrieve(query:str, top_k: int) -> List[str]:
    query_embedding = embed_chunk(query)
    results = chromadb_collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    return results['documents'][0]

query = "气候变换的最重要影响因素是什么？"
retrieved_chunks = retrieve(query, 5)

for i, chunk in enumerate(retrieved_chunks):
    print(f"[{i}] {chunk}\n")


#5. 重排（重点：设置-系统-高级-打开开发者模式!）
from sentence_transformers import CrossEncoder

def rerank(query: str, retrieved_chunks: List[str], top_k: int) -> List[str]: #用户的问题 + 召回的片段列表 + 重排后保留的片段数量
    cross_encoder = CrossEncoder('cross-encoder/mmarco-mMiniLMv2-L12-H384-v1')
    pairs = [(query, chunk) for chunk in retrieved_chunks] #用户提问和召回片段的对
    scores = cross_encoder.predict(pairs)

    chunk_with_score_list = [(chunk, score)
                       for chunk, score in zip(retrieved_chunks, scores)] # 召回的片段和分数放在一起构成一个列表
    chunk_with_score_list.sort(key=lambda pair: pair[1], reverse=True) #把这个列表按分数倒序

    return [chunk for chunk, _ in chunk_with_score_list][:top_k]  #单独取出其中的片段内容部分

reranked_chunks = rerank(query, retrieved_chunks, 3) #调用函数

for i, chunk in enumerate(reranked_chunks):
    print(f"[{i}] {chunk}\n")

#6. 最后

from dotenv import load_dotenv
from google import genai
from typing import List  # ✅ 必须导入

load_dotenv()
google_client = genai.Client()

def generate(query: str, chunks: List[str]) -> str:
    prompt = f"""你是一位知识助手，请根据用户的问题和下列片段生成准确的回答。

用户问题：{query}

相关片段：
{"\n\n".join(chunks)}  # ✅ 注意：不要有空格

请基于上述内容作答，不要编造信息。"""

    print(f"{prompt}\n\n---\n")  # ✅ 注意：外面有一个 }，里面有一个 }

    response = google_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


# ========== 调用 ==========
# 注意：这里要用 reranked_chunks，而不是 remarked_chunks
query = "气候变换的最重要影响因素是什么？"
answer = generate(query, reranked_chunks)  # ✅ 使用重排后的结果
print(answer)