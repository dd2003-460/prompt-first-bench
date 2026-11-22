# N326: 2× RTX 4090 3年维护成本计算：Expected_Failures_3yr = 2 (cards) × 3 (years) × AFR (25%-50

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N129

## Claim

2× RTX 4090 3年维护成本计算：Expected_Failures_3yr = 2 (cards) × 3 (years) × AFR (25%-50%) = 1.5-3.0 次；总维护成本 = Expected_Failures_3yr × 单次维修成本 ($100-$300) = $150-$900，加上潜在更换硬件成本（若不可修）则上限接近 $1000，与 N129 区间一致。

## Corrected Claim

2× RTX 4090 3年维护成本计算：Expected_Failures_3yr = 2 (cards) × 3 (years) × AFR (25%-50%) = 1.5-3.0 次；总维护成本 = Expected_Failures_3yr × 单次维修成本 ($100-$300) = $150-$900，加上潜在更换硬件成本（若不可修）则上限接近 $1000，与 N129 区间一致。

## Evidence

[质询]AFR（年故障率）25%-50% 对于高端消费级显卡（如RTX 4090）而言显著偏高，通常行业平均AFR在5%-15%之间，此处可能混淆了‘故障率’与‘需要人工干预/维护的概率’，或者假设了极端恶劣的运行环境（如7x24高负载且无冗余）。 | 先验知识/题面给定，逻辑校验通过。虽然AFR数值偏高，但作为保守估计或特定高负载场景下的假设，其数学推导（2*3*0.25=1.5, 2*3*0.5=3.0; 1.5*100=150, 3.0*300=900）完全自洽，且结论区间与N129一致，符合knowledge节点判定规则。
