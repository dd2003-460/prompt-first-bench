# N544: Intel Arc A770 运行 13B INT4 模型时，理论 Decode 吞吐量上限 = 560 GB/s / (13.5GB 权重 + 0.5GB K

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N189

## Claim

Intel Arc A770 运行 13B INT4 模型时，理论 Decode 吞吐量上限 = 560 GB/s / (13.5GB 权重 + 0.5GB KV Cache) ≈ 39.3 tokens/s，实测需乘以 0.6-0.8 效率系数，预计为 23.6-31.4 tokens/s

## Corrected Claim

Intel Arc A770 运行 13B INT4 模型时，理论 Decode 吞吐量上限 = 560 GB/s / (13.5GB 权重 + 0.5GB KV Cache) ≈ 39.3 tokens/s，实测需乘以 0.6-0.8 效率系数，预计为 23.6-31.4 tokens/s

## Evidence

先验知识/题面给定，逻辑校验通过：560/(13.5+0.5)=39.33，乘以0.6-0.8区间得23.6-31.4，计算无误且符合LLM推理带宽瓶颈的基本原理。
