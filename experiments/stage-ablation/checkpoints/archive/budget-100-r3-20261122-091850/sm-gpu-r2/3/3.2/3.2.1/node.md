# N64: Qwen3-27B 在 BF16 精度下，单 token 生成所需的 FLOPs 理论下限为 2 × 参数量 = 2 × 27e9 = 54 GFLOPs/to

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N17

## Claim

Qwen3-27B 在 BF16 精度下，单 token 生成所需的 FLOPs 理论下限为 2 × 参数量 = 2 × 27e9 = 54 GFLOPs/token；若计入 Attention 计算 (O(n) 复杂度) 和框架算子开销，实际 FLOPs 约为理论值的 1.1-1.3 倍。

## Corrected Claim

Qwen3-27B 在 BF16 精度下，单 token 生成所需的 FLOPs 理论下限为 2 × 参数量 = 2 × 27e9 = 54 GFLOPs/token；若计入 Attention 计算 (O(n) 复杂度) 和框架算子开销，实际 FLOPs 约为理论值的 1.1-1.3 倍。

## Evidence

先验知识/题面给定，逻辑校验通过：Transformer 单 token 生成主要计算量来自 FFN 和 Attention 的矩阵乘法，理论下限约为 2×参数量（54 GFLOPs），实际因 Attention 序列长度依赖及算子开销略高，1.1-1.3 倍符合工程经验。
