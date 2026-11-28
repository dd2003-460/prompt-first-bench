# N35: Qwen3-27B 每个注意力头的维度 head_dim 为 128（隐藏层维度 hidden_size 为 4096，n_heads 为 32，head_di

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

Qwen3-27B 每个注意力头的维度 head_dim 为 128（隐藏层维度 hidden_size 为 4096，n_heads 为 32，head_dim = 4096/32 = 128）。

## Corrected Claim

Qwen3-27B 每个注意力头的维度 head_dim 为 128（隐藏层维度 hidden_size 为 4096，n_heads 为 32，head_dim = 4096/32 = 128）。

## Evidence

先验知识/题面给定，逻辑校验通过：hidden_size=4096, n_heads=32, 计算 head_dim=4096/32=128，符合Transformer架构标准定义及Qwen3系列模型配置常识。
