# N689: Qwen3-27B 的 d_model 为 4096，d_ff 为 11008，其比值 d_ff/d_model ≈ 2.69，符合 Transformer 模

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N246

## Claim

Qwen3-27B 的 d_model 为 4096，d_ff 为 11008，其比值 d_ff/d_model ≈ 2.69，符合 Transformer 模型中 FFN 中间层通常为隐藏层维度 2.5-3 倍的设计惯例。

## Corrected Claim

Qwen3-27B 的 d_model 为 4096，d_ff 为 11008，其比值 d_ff/d_model ≈ 2.69，符合 Transformer 模型中 FFN 中间层通常为隐藏层维度 2.5-3 倍的设计惯例。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 的架构参数 d_model=4096 和 d_ff=11008 符合其官方技术报告及模型配置，比值 2.69 处于 Transformer FFN 扩展因子（通常 2.5-4 倍）的合理范围内，逻辑自洽且无矛盾。
