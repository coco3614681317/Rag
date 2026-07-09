import trimesh

path = r"D:\3D\datasets\.objaverse\hf-objaverse-v1\glbs\000-023\7d6a14874eed48c2b720f0d1adfe6dd9.glb"

scene = trimesh.load(path)

print(scene)

print("\n===== Scene 信息 =====")
print("Geometry 数量：", len(scene.geometry))
print("Geometry 名称：", scene.geometry.keys())

# 取出第一个 Mesh
mesh = list(scene.geometry.values())[0]

print("\n===== Mesh 信息 =====")
print(type(mesh))
print("顶点数量：", len(mesh.vertices))
print("三角面数量：", len(mesh.faces))
print("是否封闭：", mesh.is_watertight)
print("包围盒尺寸：", mesh.bounding_box.extents)