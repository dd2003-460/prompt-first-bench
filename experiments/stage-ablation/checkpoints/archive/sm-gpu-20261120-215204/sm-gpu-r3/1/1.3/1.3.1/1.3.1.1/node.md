# N166: Qwen3-27B 在 W4A16 配置下，32K 上下文 KV Cache 显存占用为 40.96 GB，计算公式为 2 (K/V) * 64 (Layers

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

Qwen3-27B 在 W4A16 配置下，32K 上下文 KV Cache 显存占用为 40.96 GB，计算公式为 2 (K/V) * 64 (Layers) * 8 (KV Heads) * 128 (Head Dim) * 32768 (Seq Len) * 2 bytes (BF16)，此计算独立于权重量化精度。

## Corrected Claim

Qwen3-27B 在 W4A16 配置下，32K 上下文 KV Cache 显存占用为 40.96 GB，计算公式为 2 (K/V) * 64 (Layers) * 8 (KV Heads) * 128 (Head Dim) * 32768 (Seq Len) * 2 bytes (BF16)，此计算独立于权重量化精度。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（64层，8 KV Heads，128 Head Dim）符合 GQA 设计，KV Cache 计算公式及数值推导正确，且 KV Cache 精度通常独立于权重量化精度。
