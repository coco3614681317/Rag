import trimesh
import open3d as o3d
import numpy as np


# 读取模型
path = r"D:\3D\datasets\.objaverse\hf-objaverse-v1\glbs\000-023\7d6a14874eed48c2b720f0d1adfe6dd9.glb"

scene = trimesh.load(path)

# 获取mesh
mesh = list(scene.geometry.values())[0]


print("原始顶点数量:", len(mesh.vertices))
print("原始面数量:", len(mesh.faces))


# 采样点云
points, face_index = trimesh.sample.sample_surface(
    mesh,
    2048
)

print("采样点数量:", len(points))


# 保存点云
pcd = o3d.geometry.PointCloud()

pcd.points = o3d.utility.Vector3dVector(points)

o3d.io.write_point_cloud(
    "pointcloud.ply",
    pcd
)

print("点云保存完成!")