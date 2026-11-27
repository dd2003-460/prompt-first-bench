# N261: H100 SXM5 在 Batch Size=1、序列长度=32K 的 Prefill 阶段（计算密集）实际功耗为 680W-700W，此时 GPU 利用率接近

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N81

## Claim

H100 SXM5 在 Batch Size=1、序列长度=32K 的 Prefill 阶段（计算密集）实际功耗为 680W-700W，此时 GPU 利用率接近 100%，功耗达到 TDP 上限。

## Corrected Claim

H100 SXM5 在 Batch Size=1、序列长度=32K 的 Prefill 阶段（计算密集）实际功耗为 680W-700W，此时 GPU 利用率接近 100%，功耗达到 TDP 上限。

## Evidence

先验知识/题面给定，逻辑校验通过
