import torch.nn as nn
from typing import List, Dict

class BaseModel(nn.Module):
    """自监督模型基类 | Base class for self-supervised models"""
    
    def __init__(self, config: Dict):
        """
        Args:
            config: 模型配置字典，包含以下键：
                input_dim: 输入特征维度
                latent_dim: 隐空间维度
                encoder_layers: 编码器层结构
                decoder_layers: 解码器层结构
                activation: 激活函数类型
                dropout: Dropout概率
        """
        super().__init__()
        self.config = config
        
        # 动态构建激活函数
        self.activation = self._get_activation(config.activation)
        self.dropout = nn.Dropout(config.dropout)
        
    def _get_activation(self, name: str) -> nn.Module:
        """激活函数工厂 | Activation function factory"""
        activations = {
            'relu': nn.ReLU,
            'leaky_relu': nn.LeakyReLU,
            'gelu': nn.GELU
        }
        return activations[name]()

    def build_layers(self, layer_dims: List[int]) -> nn.Sequential:
        """动态构建网络层 | Dynamically build network layers"""
        layers = []
        for in_dim, out_dim in zip(layer_dims[:-1], layer_dims[1:]):
            layers.extend([
                nn.Linear(in_dim, out_dim),
                self.activation,
                self.dropout
            ])
        return nn.Sequential(*layers[:-1])  # 移除最后一层的激活和Dropout

    def forward(self, x):
        raise NotImplementedError("子类必须实现前向传播 | Subclasses must implement forward pass")