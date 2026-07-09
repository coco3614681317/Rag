import json
import numpy as np
import trimesh
from sklearn.metrics.pairwise import cosine_similarity


def extract_feature(path):

    scene = trimesh.load(path)

    mesh = list(scene.geometry.values())[0]

    points, _ = trimesh.sample.sample_surface(
        mesh,
        2048
    )

    feature = np.concatenate([
        points.mean(axis=0),
        points.std(axis=0),
        points.min(axis=0),
        points.max(axis=0)
    ])

    return feature



# ======================
# 1. 加载数据库
# ======================

with open("features.json", "r") as f:
    database = json.load(f)


uids = []
features = []


for uid, item in database.items():

    uids.append(uid)
    features.append(item["feature"])


features = np.array(features)


# ======================
# 2. 指定查询模型
# ======================

query_path = r"D:\3D\datasets\.objaverse\hf-objaverse-v1\glbs\000-023\8476c4170df24cf5bbe6967222d1a42d.glb"


query_feature = extract_feature(query_path)


# ======================
# 3. 相似度搜索
# ======================

scores = cosine_similarity(
    query_feature.reshape(1,-1),
    features
)[0]


rank = np.argsort(scores)[::-1]


print("\n===== Top 5 Similar Models =====")


for i in rank[:5]:

    print(
        uids[i],
        "similarity:",
        scores[i]
    )