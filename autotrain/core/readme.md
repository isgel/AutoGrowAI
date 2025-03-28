## 使用示例

```
from autotrain.core import AutoEncoder, VariationalAutoEncoder

# 从配置文件初始化模型
cfg = {
    "input_dim": 784,
    "latent_dim": 32,
    "encoder_layers": [256, 128],
    "decoder_layers": [128, 256],
    "activation": "leaky_relu",
    "dropout": 0.1
}

# 标准自编码器
ae_model = AutoEncoder(cfg)

# 变分自编码器 
vae_model = VariationalAutoEncoder(cfg)

# 损失计算
recon_loss = ReconstructionLoss('mse')
kl_loss = KLDivergence()

# 前向传播示例
inputs = torch.randn(64, 784)
ae_output = ae_model(inputs)
vae_output, mu, logvar = vae_model(inputs)

loss = recon_loss(inputs, ae_output) 
vae_total_loss = recon_loss(inputs, vae_output) + 0.1 * kl_loss(mu, logvar)
```

## 关键特性

1. 模块化设计：
* 基础类BaseModel封装通用功能
* 各子类实现具体模型架构
* 损失函数独立模块化

2. 灵活配置：
```
# 可轻松扩展新架构
class DenoisingAE(AutoEncoder):
    def __init__(self, config):
        super().__init__(config)
        self.noise_layer = NoiseInjection()
        
    def forward(self, x):
        x_noisy = self.noise_layer(x)
        return super().forward(x_noisy)
```

3. 类型提示：

```
def build_layers(self, layer_dims: List[int]) -> nn.Sequential:
    """类型注释确保接口一致性"""
```

4. 设备感知：

```
# 模型自动继承基类的设备设置
model = AutoEncoder(cfg).to('cuda')
```

该实现提供高度可扩展的基础架构，同时保持与配置文件的紧密集成，适合自监督学习任务的需求扩展。