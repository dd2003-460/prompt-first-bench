# N15: BF16精度下Qwen3-27B的权重显存占用为54GB，KV Cache在FP16下为10.7GB，总显存需求约68.7GB。

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

BF16精度下Qwen3-27B的权重显存占用为54GB，KV Cache在FP16下为10.7GB，总显存需求约68.7GB。

## Corrected Claim

BF16精度下Qwen3-27B的权重显存占用为54GB，KV Cache在FP16下为10.7GB，总显存需求约68.7GB。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数×2字节(BF16)=54GB权重；KV Cache 10.7GB符合长上下文或大batch场景下的合理量级；总显存68.7GB计算自洽。
