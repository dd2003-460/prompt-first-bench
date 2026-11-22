# N214: 基于修正后的 Embedding 层大小 (1.16 GB BF16) 和其余参数 (27B - 0.62B Embedding = 26.38B params

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N77

## Claim

基于修正后的 Embedding 层大小 (1.16 GB BF16) 和其余参数 (27B - 0.62B Embedding = 26.38B params INT8)，Qwen3-27B 混合精度 (Embedding BF16 + Rest INT8) 的总权重显存精确计算为 1.16 GB + 26.38 GB ≈ 27.54 GB。

## Corrected Claim

基于修正后的 Embedding 层大小 (1.16 GB BF16) 和其余参数 (27B - 0.62B Embedding = 26.38B params INT8)，Qwen3-27B 混合精度 (Embedding BF16 + Rest INT8) 的总权重显存精确计算为 1.16 GB + 26.38 GB ≈ 27.54 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：1.16 GB (BF16 Embedding) + 26.38 GB (INT8 Rest) = 27.54 GB，算术正确且量纲一致。
