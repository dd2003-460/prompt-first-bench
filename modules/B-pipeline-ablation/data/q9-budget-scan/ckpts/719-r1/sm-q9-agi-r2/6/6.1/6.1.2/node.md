# N78: 在长上下文 (>32k) 场景中，定义性能下降指标为 ΔAccuracy = (Acc_32k - Acc_L) / Acc_32k，其中 L ∈ {64k, 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22, N23, N24

## Claim

在长上下文 (>32k) 场景中，定义性能下降指标为 ΔAccuracy = (Acc_32k - Acc_L) / Acc_32k，其中 L ∈ {64k, 128k, 262k}，需在 GSM8K-CoT 或 MMLU-Pro 长文变体上分别测量三个长度点的准确率以拟合衰减曲线

## Corrected Claim

在长上下文 (>32k) 场景中，定义性能下降指标为 ΔAccuracy = (Acc_32k - Acc_L) / Acc_32k，其中 L ∈ {64k, 128k, 262k}，需在 GSM8K-CoT 或 MMLU-Pro 长文变体上分别测量三个长度点的准确率以拟合衰减曲线

## Evidence

先验知识/题面给定，逻辑校验通过
