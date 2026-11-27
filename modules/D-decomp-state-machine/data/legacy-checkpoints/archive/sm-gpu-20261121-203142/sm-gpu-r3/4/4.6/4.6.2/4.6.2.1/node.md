# N305: 激活值显存占用的精确物理定义与误区澄清：在标准 Transformer 推理中，'激活值'主要指当前正在计算的层的中间状态（如 Attention 矩阵、MLP

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N98

## Claim

激活值显存占用的精确物理定义与误区澄清：在标准 Transformer 推理中，'激活值'主要指当前正在计算的层的中间状态（如 Attention 矩阵、MLP 中间层），而非所有层的累积。对于 27B 模型，单层激活值峰值取决于 Attention Head 数量和 FFN 中间维度，而非简单的 seq_len * hidden_dim。

## Corrected Claim

激活值显存占用的精确物理定义与误区澄清：在标准 Transformer 推理中，'激活值'主要指当前正在计算的层的中间状态（如 Attention 矩阵、MLP 中间层），而非所有层的累积。对于 27B 模型，单层激活值峰值取决于 Attention Head 数量和 FFN 中间维度，而非简单的 seq_len * hidden_dim。

## Evidence

先验知识/题面给定，逻辑校验通过：在标准Transformer推理中，激活值确实指当前层中间状态，且峰值显存占用由Attention矩阵（seq_len^2 * heads）和FFN中间维度（seq_len * ffn_dim）决定，而非简单的seq_len * hidden_dim，符合物理定义与工程常识。

## Search Query

Transformer inference activation memory footprint single layer vs cumulative
