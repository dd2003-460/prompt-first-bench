# N160: L40S 在 BF16 精度下，Decode 阶段（Batch=1, KV_Cache≈32.77GB, Weights≈54GB）的理论吞吐量上限为 864 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N48

## Claim

L40S 在 BF16 精度下，Decode 阶段（Batch=1, KV_Cache≈32.77GB, Weights≈54GB）的理论吞吐量上限为 864 / (32.77 + 54) ≈ 9.96 tokens/s；此数值为带宽瓶颈下的理论最大值，实测通常乘以 0.6-0.8 效率系数。

## Corrected Claim

L40S 在 BF16 精度下，Decode 阶段（Batch=1, KV_Cache≈32.77GB, Weights≈54GB）的理论吞吐量上限为 864 / (32.77 + 54) ≈ 9.96 tokens/s；此数值为带宽瓶颈下的理论最大值，实测通常乘以 0.6-0.8 效率系数。

## Evidence

先验知识/题面给定，逻辑校验通过：L40S显存带宽约864GB/s，Decode阶段Batch=1时受限于KV Cache和Weights的读取带宽，理论上限计算符合物理直觉，效率系数0.6-0.8符合工程经验。
