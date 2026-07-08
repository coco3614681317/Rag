
# 1. 配置 Conda 环境目录到 D 盘(首先保证conda优先安装在D盘（空间大的那个盘尽量不是C）)
conda config --add envs_dirs D:\minicoda\envs

# 2. 验证环境目录配置（第一行应为 D 盘路径第一行如果是D盘则确保路径已修改正确)
conda config --show envs_dirs

# 3. 查看当前所有环境(保证除了目标目录下其余位置没有安装objaverse否则_)
conda env list

# 4. 清理可能存在的旧 objaverse 环境
conda deactivate
conda env remove -n objaverse -y

# 5. 在项目目录下创建 Python 3.11 环境
conda create --prefix D:\3D\3d_rag\.conda_env python=3.11 -y

# 6. 激活环境
conda activate D:\3D\3d_rag\.conda_env

# 7. 创建测试文件（自动创建 src 目录并写入测试代码）# 目标文件夹下建立导入 objaverse 的测试PY文件
mkdir -Force D:\3D\3d_rag\src
@"
import objaverse
print("Objaverse OK!")
"@ | Out-File -FilePath D:\3D\3d_rag\src\test.py -Encoding utf8

# 8. 运行测试
python D:\3D\3d_rag\src\test.py