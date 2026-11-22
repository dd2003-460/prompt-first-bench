# N251: 算法偏差度 α 的置信区间 [α_low, α_high]，基于曝光权重数据的样本量 N_sample 和标准误 SE_α = sqrt(Var(W_high)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N74

## Claim

算法偏差度 α 的置信区间 [α_low, α_high]，基于曝光权重数据的样本量 N_sample 和标准误 SE_α = sqrt(Var(W_high)/N_high + Var(W_base)/N_base) 计算，若 α_low > 0.30 则支持 N31 中‘算法偏向高溢价’的假设，否则需重新评估置信度提升条件。

## Corrected Claim

算法偏差度 α 的置信区间 [α_low, α_high]，基于曝光权重数据的样本量 N_sample 和标准误 SE_α = sqrt(Var(W_high)/N_high + Var(W_base)/N_base) 计算，若 α_low > 0.30 则支持 N31 中‘算法偏向高溢价’的假设，否则需重新评估置信度提升条件。

## Evidence

先验知识/题面给定，逻辑校验通过
