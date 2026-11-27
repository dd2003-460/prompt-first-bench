# N49: Activation_MB 的主要组成部分：在 Transformer 解码阶段，激活内存主要包含：1. 注意力矩阵 (n_heads * seq_len * 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

Activation_MB 的主要组成部分：在 Transformer 解码阶段，激活内存主要包含：1. 注意力矩阵 (n_heads * seq_len * seq_len * bytes)，但在 Flash Attention 下不显式存储完整矩阵；2. 中间层激活 (intermediate_size * seq_len * batch * bytes)；3. 残差流 (hidden_size * seq_len * batch * bytes)。

## Corrected Claim

Activation_MB 的主要组成部分：在 Transformer 解码阶段，激活内存主要包含：1. 注意力矩阵 (n_heads * seq_len * seq_len * bytes)，但在 Flash Attention 下不显式存储完整矩阵；2. 中间层激活 (intermediate_size * seq_len * batch * bytes)；3. 残差流 (hidden_size * seq_len * batch * bytes)。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

transformer activation memory components flash attention
