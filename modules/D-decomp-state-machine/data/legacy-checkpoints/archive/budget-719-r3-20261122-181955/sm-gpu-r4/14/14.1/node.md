# N388: AMD Radeon Pro W7900 48GB 在 32K 上下文、BF16 精度下，理论 Decode 吞吐量上限为 800 GB/s / (54 GB 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N130

## Claim

AMD Radeon Pro W7900 48GB 在 32K 上下文、BF16 精度下，理论 Decode 吞吐量上限为 800 GB/s / (54 GB 权重 + 8.59 GB KV Cache) ≈ 12.6 tokens/s，实测需乘以 0.6-0.8 效率系数，预计为 7.6-10.1 tokens/s。

## Corrected Claim

AMD Radeon Pro W7900 48GB 在 32K 上下文、BF16 精度下，理论 Decode 吞吐量上限为 800 GB/s / (54 GB 权重 + 8.59 GB KV Cache) ≈ 12.6 tokens/s，实测需乘以 0.6-0.8 效率系数，预计为 7.6-10.1 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：带宽除以总显存占用（权重+KV Cache）符合Decode阶段内存带宽瓶颈的理论上限计算逻辑，数值量级合理。
