1. Key Parameter Notes:
Model Architecture

encoder_layers/decoder_layers: Layer dimensions for autoencoder

latent_dim: Bottleneck dimension for feature compression

2. Data Augmentation

```
augment_methods:
  - random_mask:      # Random masking
      ratio: 0.2     # Mask ratio
  - channel_swap:    # Channel permutation
      prob: 0.5      # Application probability
```

3. Learning Rate Scheduling
```
lr_scheduler:
  name: "cosine"
  params:
    warmup_epochs: 5  # Learning rate warmup epochs
    min_lr: 1e-6       # Minimum learning rate
```

4. Distributed Training

```
distributed:
  enable: False       # Enable distributed training
  backend: "nccl"     # Communication backend
  nodes: 1            # Number of nodes
  gpus_per_node: 8    # GPUs per node
```