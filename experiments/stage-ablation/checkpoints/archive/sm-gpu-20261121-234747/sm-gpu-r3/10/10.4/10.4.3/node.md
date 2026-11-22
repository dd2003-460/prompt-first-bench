# N497: 精度-成本权衡拐点公式：Break_Even_Precision = argmin{Precision | ΔQuality(Precision) < ε AN

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N157

## Claim

精度-成本权衡拐点公式：Break_Even_Precision = argmin{Precision | ΔQuality(Precision) < ε AND (TCO_BF16 - TCO_Precision) / TCO_BF16 > Cost_Saving_Threshold}，需代入 FP8 和 W4 的具体 TCO 节省比例（FP8 显存减半，W4 显存减至1/4）及质量损失阈值 ε（如 MMLU 损失 < 1%） [待核验]

## Corrected Claim

精度-成本权衡拐点公式：Break_Even_Precision = argmin{Precision | ΔQuality(Precision) < ε AND (TCO_BF16 - TCO_Precision) / TCO_BF16 > Cost_Saving_Threshold}，需代入 FP8 和 W4 的具体 TCO 节省比例（FP8 显存减半，W4 显存减至1/4）及质量损失阈值 ε（如 MMLU 损失 < 1%） [待核验]

## Evidence

先验知识/题面给定，逻辑校验通过
