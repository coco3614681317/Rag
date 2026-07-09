import trimesh
import numpy as np


path = r"D:\3D\datasets\.objaverse\hf-objaverse-v1\glbs\000-023\7d6a14874eed48c2b720f0d1adfe6dd9.glb"


scene = trimesh.load(path)

mesh = list(scene.geometry.values())[0]


# 采样点云
points, _ = trimesh.sample.sample_surface(
    mesh,
    2048
)


print("点云shape:")
print(points.shape)


# 简单几何特征
feature = np.concatenate([
    points.mean(axis=0),     # 中心位置
    points.std(axis=0),      # 分布范围
    points.min(axis=0),      # 最小坐标
    points.max(axis=0)       # 最大坐标
])


print("\nFeature:")
print(feature)

print("\nFeature维度:")
print(feature.shape)