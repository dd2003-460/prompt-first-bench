# N217: 基于修正后的 Embedding 层大小 (1.16 GB BF16) 和其余参数 (26.38B params W4/0.5 bytes)，Qwen3-27B

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N78

## Claim

基于修正后的 Embedding 层大小 (1.16 GB BF16) 和其余参数 (26.38B params W4/0.5 bytes)，Qwen3-27B 混合精度 (Embedding BF16 + Rest W4) 的总权重显存精确计算为 1.16 GB + 13.19 GB ≈ 14.35 GB。

## Corrected Claim

基于修正后的 Embedding 层大小 (1.16 GB BF16) 和其余参数 (26.38B params W4/0.5 bytes)，Qwen3-27B 混合精度 (Embedding BF16 + Rest W4) 的总权重显存精确计算为 1.16 GB + 13.19 GB ≈ 14.35 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：1.16 GB + 13.19 GB = 14.35 GB，算术正确且量级合理。
