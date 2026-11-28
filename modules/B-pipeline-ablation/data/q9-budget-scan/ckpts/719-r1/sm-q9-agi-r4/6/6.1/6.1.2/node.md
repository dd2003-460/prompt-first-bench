# N78: 在长上下文 (>32k) 场景中，定义性能下降指标为 ΔAccuracy = (Acc_32k - Acc_L) / Acc_32k，其中 L ∈ {64k, 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N22, N23, N24

## Claim

在长上下文 (>32k) 场景中，定义性能下降指标为 ΔAccuracy = (Acc_32k - Acc_L) / Acc_32k，其中 L ∈ {64k, 128k, 262k}，需在 GSM8K-CoT 或 MMLU-Pro 长文变体上分别测量三个长度点的准确率以拟合衰减曲线

## Corrected Claim

在长上下文 (>32k) 场景中，定义性能下降指标为 ΔAccuracy = (Acc_32k - Acc_L) / Acc_32k，其中 L ∈ {64k, 128k, 262k}，需在 GSM8K-CoT 或 MMLU-Pro 长文变体上分别测量三个长度点的准确率以拟合衰减曲线

## Evidence

父节点级核验未通过：不完备（子节点存在定义冲突且覆盖不全。1. 矛盾：父节点定义 ΔAccuracy 基于 'Acc_32k' 作为基准，而子节点2将 ΔAcc 重新定义为 '(Acc_noisy - Acc_clean) / Acc_clean'，两者基准和分子含义均不一致，导致逻辑断裂。2. 不完备：父节点明确要求在 'GSM8K-CoT 或 MMLU-Pro' 上测量，但子节点仅提供了 GSM8K 的构造方法，完全缺失 MMLU-Pro 长文变体的构造或测量方案。）
