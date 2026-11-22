# N119: RTX 3090 的显存带宽为 936 GB/s，在 INT8 下 Decode 阶段理论最大吞吐量为 936 GB/s / 27 GB ≈ 34.7 toke

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N34

## Claim

RTX 3090 的显存带宽为 936 GB/s，在 INT8 下 Decode 阶段理论最大吞吐量为 936 GB/s / 27 GB ≈ 34.7 tokens/s，考虑 85% 实际效率后约为 29.5 tokens/s。

## Corrected Claim

RTX 3090 的显存带宽为 936 GB/s，在 INT8 下 Decode 阶段理论最大吞吐量为 936 GB/s / 27 GB ≈ 34.7 tokens/s，考虑 85% 实际效率后约为 29.5 tokens/s。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别针对父节点中的三个核心要素（硬件带宽参数、效率系数假设、精度/架构对比）进行了独立且互不重叠的分析。节点1验证输入参数，节点2修正中间计算系数，节点3提供对比场景验证结论边界，逻辑上正交且共同构成了对父节点结论的完整审计。）
