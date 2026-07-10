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


#导入大模型ULIP
cd D:\3D\3d_rag\models

git clone https://github.com/salesforce/ULIP.git

    # 1. 确认 ULIP 有 README 文件
    dir README*

    # 2. 搜索 "encode_pc" 在哪里定义/使用
    findstr /S /I "encode_pc" *.py

    # 3. 搜索 "load_state_dict" 看看怎么加载模型
    findstr /S /I "load_state_dict" *.py


    # 从 ULIP_models.py 看出来的用法
    from models.ULIP_models import ULIP_Model

# 加载模型
model = ULIP_Model()
model.load_state_dict(torch.load('checkpoint.pth'))

# 编码点云
pc_features = model.encode_pc(pointcloud)

# 1） 搜索 "get_model" 函数在哪里定义/使用
findstr /S /I "get_model(" *.py
# 结果：在 main.py 里使用，在 utils.py 里定义

# 2） 搜索 "pc_projection" 投影层
findstr /S /I "pc_projection" *.py
# 结果：在 ULIP_models.py 里，点云特征→文本空间的投影层



# 1️⃣ 构建模型
# 找模型类定义
findstr /S /I "class.*Net" *.py
findstr /S /I "class.*Model" *.py

# 找模型构建函数
findstr /S /I "def.*model" *.py
findstr /S /I "def build" *.py

# 找具体的模型实例化（如 ULIP_PointBERT）
findstr /S /I "ULIP_PointBERT" *.py
model = ULIP_PointBERT(args)

# 2️⃣ 加载权重
# 找 torch.load 的所有出现
findstr /S /I "torch.load" *.py

# 找 load_state_dict
findstr /S /I "load_state_dict" *.py

# 找 from_pretrained（HuggingFace 风格）
findstr /S /I "from_pretrained" *.py
checkpoint = torch.load('pretrained.pth')

# 3️⃣ 恢复状态
# 找 load_state_dict
findstr /S /I "load_state_dict" *.py

# 找 checkpoint 加载
findstr /S /I "checkpoint" *.py
findstr /S /I "ckpt" *.py

# 找 resume 相关
findstr /S /I "resume" *.py
model.load_state_dict(checkpoint['model_state_dict'])

# 4️⃣ 提取特征/推理
# 找 forward 方法
findstr /S /I "def forward" *.py

# 找 encode 方法（点云、文本、图像）
findstr /S /I "def encode" *.py

# 找具体的编码函数
findstr /S /I "encode_pc" *.py
findstr /S /I "encode_text" *.py
findstr /S /I "encode_image" *.py

# 找 extract 方法
findstr /S /I "def extract" *.py
embedding = model.encode_pc(pc)


ULIP = SLIP + PointBERT
ULIP2 = OpenCLIP + PointBERT + Colors