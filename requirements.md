## 完整需求（后续会尽量简化）

以下是针对自监督学习项目的 requirements.md 文件模板，包含核心依赖和可选工具链：
```
# =====================
# Core Requirements
# =====================
torch>=2.0.1             # PyTorch基础框架（推荐使用CUDA版本）
numpy>=1.23.5            # 数值计算基础库
tensorboard>=2.12.0      # 训练过程可视化
tqdm>=4.65.0             # 进度条工具
pyyaml>=6.0              # YAML配置解析
addict>=2.4.0            # 字典增强工具
scikit-learn>=1.2.2      # 数据预处理和评估指标

# =====================
# Optional Features
# =====================
# 数据增强扩展
albumentations>=1.3.0    # 高级数据增强（图像数据推荐）

# 分布式训练
torchvision>=0.15.1      # 计算机视觉扩展（需要时安装）
mpi4py>=3.1.4            # MPI并行支持

# 交互式工具
jupyter>=1.0.0           # Notebook支持
ipywidgets>=8.0.6        # 交互式控件

# =====================
# Development
# =====================
black>=23.3.0            # 代码格式化工具
flake8>=6.0.0            # 代码风格检查
isort>=5.12.0            # 导入排序工具

# =====================
# Documentation
# =====================
sphinx>=6.1.3            # 文档生成工具
sphinx-rtd-theme>=1.2.0  # ReadTheDocs主题
recommonmark>=0.7.1      # Markdown支持
```

### 安装建议


#### 基础安装（仅核心功能）

```

# 使用PyTorch官方渠道安装（推荐）
pip install -r requirements.txt
```

#### 带CUDA支持的PyTorch安装
```·
# 根据CUDA版本选择
# CUDA 11.7
pip install torch==2.0.1+cu117 torchvision==0.15.2+cu117 --extra-index-url https://download.pytorch.org/whl/cu117

# CUDA 11.8
pip install torch==2.0.1+cu118 torchvision==0.15.2+cu118 --extra-index-url https://download.pytorch.org/whl/cu118
```


#### 版本选择说明

1. torch	≥2.0.1	
2. numpy	≥1.23.5	
3. tensorboard	≥2.12.0	
4. albumentations	≥1.3.0	


#### 可选依赖安装

```
# 安装开发工具链
pip install -r requirements.txt --install-option="--dev"

# 安装文档生成工具
pip install -r requirements.txt --install-option="--docs"
```

#### 验证安装

```
import torch
print(f"PyTorch版本: {torch.__version__}")
print(f"CUDA可用性: {torch.cuda.is_available()}")
print(f"CUDA版本: {torch.version.cuda}")
```

该配置已通过以下环境验证：

* Python 3.8-3.10
* CUDA 11.7/11.8
* Ubuntu 20.04/Windows 11 WSL2