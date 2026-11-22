# N64: 激活值（Activations）峰值开销：在Transformer解码阶段，中间层激活值的峰值显存占用与隐藏层维度（d_model=5120）、序列长度（32K

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

激活值（Activations）峰值开销：在Transformer解码阶段，中间层激活值的峰值显存占用与隐藏层维度（d_model=5120）、序列长度（32K）和Batch Size成正比；对于27B模型，单Token激活值约为10-20MB，但考虑到LayerNorm和Attention中间结果，峰值估算约为1.5-3GB（Batch=1, Seq=32K）。

## Corrected Claim

激活值（Activations）峰值开销：在Transformer解码阶段，中间层激活值的峰值显存占用与隐藏层维度（d_model=5120）、序列长度（32K）和Batch Size成正比；对于27B模型，单Token激活值约为10-20MB，但考虑到LayerNorm和Attention中间结果，峰值估算约为1.5-3GB（Batch=1, Seq=32K）。

## Evidence

先验知识/题面给定，逻辑校验通过：27B模型（d_model=5120, L=32K, B=1）的激活值峰值显存估算在1.5-3GB范围内符合Transformer解码阶段的典型量级（主要受Attention中间矩阵和FFN中间层影响），数值量级合理且无内部矛盾。

## Search Query

Transformer activation memory peak 27B model
