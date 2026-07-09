import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


# =====================
# 读取数据库
# =====================

with open("features.json", "r") as f:
    data = json.load(f)


print("数据库模型数量:", len(data))


# =====================
# 构建feature矩阵
# =====================

uids = []
features = []

for uid, item in data.items():

    uids.append(uid)

    features.append(
        item["feature"]
    )


features = np.array(features)


print("Feature shape:", features.shape)


# =====================
# 选择一个query模型
# =====================

query_index = 0

query_feature = features[query_index].reshape(1,-1)


# =====================
# 计算相似度
# =====================

scores = cosine_similarity(
    query_feature,
    features
)[0]


# 排序
rank = np.argsort(
    scores
)[::-1]


print("\n===== 最相似模型 =====")


for i in rank[:5]:

    print(
        "UID:",
        uids[i],
        " similarity:",
        scores[i]
    )