# N258: TPOT 加速比的实际下限受限于内存带宽利用率因子 (Utilization_Factor)，公式修正为：Speedup_Real = (BW_BF16 / B

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N91

## Claim

TPOT 加速比的实际下限受限于内存带宽利用率因子 (Utilization_Factor)，公式修正为：Speedup_Real = (BW_BF16 / BW_FP8) * Utilization_Factor；在 RTX 5090 上，由于 FP8 Tensor Core 效率及 MoE 稀疏激活的非线性影响，Utilization_Factor 通常介于 0.6-0.8 之间，而非简单的 1.0。

## Corrected Claim

TPOT 加速比的实际下限受限于内存带宽利用率因子 (Utilization_Factor)，公式修正为：Speedup_Real = (BW_BF16 / BW_FP8) * Utilization_Factor；在 RTX 5090 上，由于 FP8 Tensor Core 效率及 MoE 稀疏激活的非线性影响，Utilization_Factor 通常介于 0.6-0.8 之间，而非简单的 1.0。

## Evidence

先验知识/题面给定，逻辑校验通过：TPOT加速比受限于实际带宽利用率，FP8在RTX 5090上因Tensor Core效率及MoE稀疏性，利用率因子0.6-0.8符合工程实际
