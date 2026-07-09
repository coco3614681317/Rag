import objaverse

print("正在获取 UID...")

uids = objaverse.load_uids()

print(f"共有 {len(uids)} 个模型")

print("开始下载前10个模型...")

objects = objaverse.load_objects(
    uids=uids[:10]
)

print("下载完成！")
print(objects)