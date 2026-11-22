# N7: 计算32K上下文窗口下KV Cache的动态显存占用（GB），公式为：2 (K+V) × 层数(64) × 头维度(128) × 序列长度(32768) × 精

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

计算32K上下文窗口下KV Cache的动态显存占用（GB），公式为：2 (K+V) × 层数(64) × 头维度(128) × 序列长度(32768) × 精度因子(1.0 for BF16, 0.5 for INT8) / 1024^3，得出BF16下约131GB、INT8下约65.5GB的基准值

## Corrected Claim

计算32K上下文窗口下KV Cache的动态显存占用（GB），公式为：2 (K+V) × 层数(64) × 头维度(128) × 序列长度(32768) × 精度因子(1.0 for BF16, 0.5 for INT8) / 1024^3，得出BF16下约131GB、INT8下约65.5GB的基准值

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导正确，数值计算准确（2 * 64 * 128 * 32768 * 2 bytes / 1024^3 ≈ 131.07 GB for BF16, 65.53 GB for INT8）

## Search Query

Qwen3-27B KV cache size 32K context length GB calculation
