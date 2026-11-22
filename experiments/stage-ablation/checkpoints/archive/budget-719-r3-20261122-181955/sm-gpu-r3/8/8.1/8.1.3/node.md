# N347: 量化损失 $\Delta MMLU = MMLU_{BF16} - MMLU_{INT4}$ 的置信区间通过 5 次独立随机种子重跑取均值和标准差，若标准差 >

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N117

## Claim

量化损失 $\Delta MMLU = MMLU_{BF16} - MMLU_{INT4}$ 的置信区间通过 5 次独立随机种子重跑取均值和标准差，若标准差 > 0.5%，则需增加评测样本量至 10 次以稳定估计。

## Corrected Claim

量化损失 $\Delta MMLU = MMLU_{BF16} - MMLU_{INT4}$ 的置信区间通过 5 次独立随机种子重跑取均值和标准差，若标准差 > 0.5%，则需增加评测样本量至 10 次以稳定估计。

## Evidence

先验知识/题面给定，逻辑校验通过
