import torch
from .base_model import BaseModel

class AutoEncoder(BaseModel):
    """标准自编码器 | Vanilla Autoencoder"""
    
    def __init__(self, config: Dict):
        super().__init__(config)
        
        # 构建编码器
        encoder_dims = [config.input_dim] + config.encoder_layers + [config.latent_dim]
        self.encoder = self.build_layers(encoder_dims)
        
        # 构建解码器
        decoder_dims = [config.latent_dim] + config.decoder_layers + [config.input_dim]
        self.decoder = self.build_layers(decoder_dims)
        
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """前向传播 | Forward pass"""
        z = self.encoder(x)
        x_recon = self.decoder(z)
        return x_recon

    def encode(self, x: torch.Tensor) -> torch.Tensor:
        """特征编码 | Feature encoding"""
        with torch.no_grad():
            return self.encoder(x)