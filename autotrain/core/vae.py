import torch
from .base_model import BaseModel

class VariationalAutoEncoder(BaseModel):
    """变分自编码器 | Variational Autoencoder (VAE)"""
    
    def __init__(self, config: Dict):
        super().__init__(config)
        
        # 编码器网络
        encoder_dims = [config.input_dim] + config.encoder_layers
        self.encoder = self.build_layers(encoder_dims)
        
        # 均值和对数方差层
        self.fc_mu = nn.Linear(encoder_dims[-1], config.latent_dim)
        self.fc_logvar = nn.Linear(encoder_dims[-1], config.latent_dim)
        
        # 解码器网络
        decoder_dims = [config.latent_dim] + config.decoder_layers
        self.decoder = self.build_layers(decoder_dims)
        self.fc_out = nn.Linear(decoder_dims[-1], config.input_dim)
        
    def reparameterize(self, mu: torch.Tensor, logvar: torch.Tensor) -> torch.Tensor:
        """重参数化技巧 | Reparameterization trick"""
        std = torch.exp(0.5*logvar)
        eps = torch.randn_like(std)
        return mu + eps*std
        
    def forward(self, x: torch.Tensor) -> tuple:
        """前向传播 | Forward pass"""
        # 编码
        h = self.encoder(x)
        mu, logvar = self.fc_mu(h), self.fc_logvar(h)
        z = self.reparameterize(mu, logvar)
        
        # 解码
        x_recon = self.fc_out(self.decoder(z))
        return x_recon, mu, logvar