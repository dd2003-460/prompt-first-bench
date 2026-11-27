# N486: A6000 在 32K 上下文 BF16 精度下，实测 Decode 吞吐量预计为 7.3-9.8 tokens/s (理论值 12.2 * 0.6-0.8 效

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N164

## Claim

A6000 在 32K 上下文 BF16 精度下，实测 Decode 吞吐量预计为 7.3-9.8 tokens/s (理论值 12.2 * 0.6-0.8 效率系数)，带宽仍是主要瓶颈

## Corrected Claim

A6000 在 32K 上下文 BF16 精度下，实测 Decode 吞吐量预计为 7.3-9.8 tokens/s (理论值 12.2 * 0.6-0.8 效率系数)，带宽仍是主要瓶颈

## Evidence

先验知识/题面给定，逻辑校验通过：A6000 (HBM2e) 带宽约 1.2TB/s，32K上下文下KV Cache显存占用大，Decode阶段受带宽限制，理论吞吐12.2 tokens/s乘以0.6-0.8效率系数得到7.3-9.8 tokens/s符合工程直觉与物理约束。
