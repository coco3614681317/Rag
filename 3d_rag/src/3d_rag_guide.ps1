#处理本地3D数据
conda activate D:\3D\3d_rag\.conda_env
cd D:\3D\3d_rag  #激活conda环境并进入目标文件夹

mklink /J "C:\Users\Administrator\.objaverse" "D:\3D\datasets\.objaverse" #管理员模式将下载的模型改到D盘
python src\download_objaverse.py  #下载10个模型


pip install trimesh  #下载读取包
python src\read_glb.py #加载模型信息


pip install open3d  #下载模型转换点云包
python src\mesh_to_pointcloud.py  # 点云转换测试

python src\view_pointcloud.py


python src\extract_all_features.py # 正式批处理

pip install scikit-learn

python src\search_similar.py #库内比对相似模型

python src\query_model.py #任意新的GLB跟库内比对
    ===== Top 5 Similar Models =====
    8476c4170df24cf5bbe6967222d1a42d similarity: 0.999987264127369
    c786b97d08b94d02a1fa3b87d2e86cf1 similarity: 0.7744038995422129
    7d6a14874eed48c2b720f0d1adfe6dd9 similarity: 0.7415152391978678
    8ff7f1f2465347cd8b80c9b206c2781e similarity: 0.42896657997549503
    efd35e7d21ac482688c294e3b6c9f74e similarity: 0.3632399977628492


#导入大模型
cd D:\3D\3d_rag\models

git clone https://github.com/salesforce/ULIP.git

# 1. 确认 ULIP 有 README 文件
dir README*

# 2. 搜索 "encode_pc" 在哪里定义/使用
findstr /S /I "encode_pc" *.py

# 3. 搜索 "load_state_dict" 看看怎么加载模型
findstr /S /I "load_state_dict" *.py