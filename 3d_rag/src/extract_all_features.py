import objaverse
import trimesh
import numpy as np
import json
import os


# =========================
# 1. 获取模型路径
# =========================

print("正在获取Objaverse模型...")

uids = objaverse.load_uids()

# 测试阶段先处理10个
uids = uids[:10]

objects = objaverse.load_objects(
    uids=uids
)

print(f"获取到 {len(objects)} 个模型")


# =========================
# 2. 提取feature
# =========================

results = {}

for uid, path in objects.items():

    print("\n正在处理:", uid)

    try:

        # 读取GLB
        scene = trimesh.load(path)


        # 获取mesh
        mesh = list(scene.geometry.values())[0]


        # Mesh采样点云
        points, _ = trimesh.sample.sample_surface(
            mesh,
            2048
        )


        # 简单feature
        feature = np.concatenate([
            points.mean(axis=0),
            points.std(axis=0),
            points.min(axis=0),
            points.max(axis=0)
        ])


        results[uid] = {
            "path": path,
            "feature": feature.tolist()
        }


        print("完成")


    except Exception as e:

        print("失败:", e)



# =========================
# 3. 保存结果
# =========================

output = "features.json"

with open(output, "w") as f:
    json.dump(
        results,
        f,
        indent=2
    )


print("\n全部完成!")
print("保存到:", output)