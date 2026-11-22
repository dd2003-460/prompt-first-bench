# N23: 量化精度对 TTFT/TPOT 的线性影响系数：FP8/INT8 相比 BF16 将权重体积减半，理论上 TPOT 降低约 50%，但需量化计算精度损失带来的 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

量化精度对 TTFT/TPOT 的线性影响系数：FP8/INT8 相比 BF16 将权重体积减半，理论上 TPOT 降低约 50%，但需量化计算精度损失带来的 Re-computation 或 Accuracy Drop 是否触发额外的校准开销或精度恢复步骤的时间成本。

## Corrected Claim

量化精度对 TTFT/TPOT 的线性影响系数：FP8/INT8 相比 BF16 将权重体积减半，理论上 TPOT 降低约 50%，但需量化计算精度损失带来的 Re-computation 或 Accuracy Drop 是否触发额外的校准开销或精度恢复步骤的时间成本。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8/INT8相比BF16权重体积减半，理论上TPOT降低约50%符合基本计算逻辑，量化精度损失带来的额外开销属于合理工程考量。
