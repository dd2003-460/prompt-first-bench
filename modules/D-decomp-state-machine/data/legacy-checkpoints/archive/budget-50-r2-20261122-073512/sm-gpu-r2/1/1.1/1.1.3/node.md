# N41: KV Cache 显存占用的计算公式：2 (K/V) × L (layers) × H (head_dim) × C (context_len) × P (by

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

KV Cache 显存占用的计算公式：2 (K/V) × L (layers) × H (head_dim) × C (context_len) × P (bytes_per_param)，其中 L=32, H=128, C=32768, P=2 (BF16)

## Corrected Claim

KV Cache 显存占用的计算公式：2 (K/V) × L (layers) × H (head_dim) × C (context_len) × P (bytes_per_param)，其中 L=32, H=128, C=32768, P=2 (BF16)

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合Transformer KV Cache标准计算逻辑（2代表K和V，L为层数，H为头维度，C为上下文长度，P为字节数），数值量级合理（32层*128维*32768长*2字节*2(K/V) ≈ 512MB/序列，符合BF16精度下长上下文显存占用常识）。
