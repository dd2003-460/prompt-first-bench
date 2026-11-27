# N245: 基于修正后的显存占用 (37.74 GB)，L40S (864 GB/s 带宽) 运行 INT8 权重 + BF16 KV 的解码速度理论峰值为 32 Toke

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N85

## Claim

基于修正后的显存占用 (37.74 GB)，L40S (864 GB/s 带宽) 运行 INT8 权重 + BF16 KV 的解码速度理论峰值为 32 Tokens/s (864 GB/s / 27 GB 权重)，考虑 85% 内存效率后实际约为 27 Tokens/s，该方案无需量化 KV Cache 即可满足 32K 上下文需求，消除了 N85 提出的 '必须使用 FP8 权重或 KV 量化' 的强制约束。

## Corrected Claim

基于修正后的显存占用 (37.74 GB)，L40S (864 GB/s 带宽) 运行 INT8 权重 + BF16 KV 的解码速度理论峰值为 32 Tokens/s (864 GB/s / 27 GB 权重)，考虑 85% 内存效率后实际约为 27 Tokens/s，该方案无需量化 KV Cache 即可满足 32K 上下文需求，消除了 N85 提出的 '必须使用 FP8 权重或 KV 量化' 的强制约束。

## Evidence

先验知识/题面给定，逻辑校验通过：864 GB/s / 27 GB ≈ 32 Tokens/s，32 * 0.85 = 27.2 ≈ 27 Tokens/s，计算自洽且符合硬件带宽限制解码的理论模型。
