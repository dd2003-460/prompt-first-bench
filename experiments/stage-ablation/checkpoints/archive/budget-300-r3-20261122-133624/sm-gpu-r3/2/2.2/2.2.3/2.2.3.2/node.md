# N254: N73 替代工作点（高性/大显存单卡 BF16）：1× A100 80GB (2039 GB/s 带宽)，BF16 权重 54GB，KV Cache (32K 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N73

## Claim

N73 替代工作点（高性/大显存单卡 BF16）：1× A100 80GB (2039 GB/s 带宽)，BF16 权重 54GB，KV Cache (32K ctx) 约 4-6GB，总占用 < 80GB。理论 Decode 上限 = 2039 / 54 ≈ 37.8 tokens/s，实际 85% 效率 ≈ 32.1 tokens/s。此方案无需多卡互联，电力成本同 N138，但硬件成本远高于消费级卡。

## Corrected Claim

N73 替代工作点（高性/大显存单卡 BF16）：1× A100 80GB (2039 GB/s 带宽)，BF16 权重 54GB，KV Cache (32K ctx) 约 4-6GB，总占用 < 80GB。理论 Decode 上限 = 2039 / 54 ≈ 37.8 tokens/s，实际 85% 效率 ≈ 32.1 tokens/s。此方案无需多卡互联，电力成本同 N138，但硬件成本远高于消费级卡。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB 带宽 2039 GB/s 与 BF16 权重 54GB 符合硬件规格，带宽瓶颈计算 2039/54≈37.8 正确，内存占用 54+6=60GB < 80GB 自洽。

## Search Query

A100 80GB HBM2e bandwidth GB/s
