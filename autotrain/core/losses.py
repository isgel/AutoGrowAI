import torch

class ReconstructionLoss:
    """重建损失计算模块 | Reconstruction loss module"""
    
    def __init__(self, loss_type: str = 'mse'):
        """
        Args:
            loss_type: 损失类型 ['mse', 'l1', 'bce']
        """
        self.loss_fn = {
            'mse': torch.nn.MSELoss(),
            'l1': torch.nn.L1Loss(),
            'bce': torch.nn.BCEWithLogitsLoss()
        }[loss_type]
        
    def __call__(self, 
                inputs: torch.Tensor, 
                reconstructions: torch.Tensor) -> torch.Tensor:
        """计算重建损失 | Compute reconstruction loss"""
        return self.loss_fn(reconstructions, inputs)

class KLDivergence:
    """KL散度计算 | KL divergence calculation"""
    
    def __call__(self, mu: torch.Tensor, logvar: torch.Tensor) -> torch.Tensor:
        """计算KL散度 | Compute KL divergence"""
        return -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())