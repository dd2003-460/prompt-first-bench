# N118: 性价比核心指标定义为 'Effective Throughput per Dollar (ETPD)'，计算公式为 ETPD = (Tokens_per_sec

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

性价比核心指标定义为 'Effective Throughput per Dollar (ETPD)'，计算公式为 ETPD = (Tokens_per_second * Quality_Score) / (Initial_Cost + 3yr_Power_Cost + 3yr_Maintenance_Cost)。其中 Quality_Score 需归一化至 0-1 区间（基于 MMLU/HumanEval 相对 BF16 的保留率），以量化精度损失对有效性能的影响，避免单纯追求高吞吐而忽视输出质量不可接受的情况。

## Corrected Claim

性价比核心指标定义为 'Effective Throughput per Dollar (ETPD)'，计算公式为 ETPD = (Tokens_per_second * Quality_Score) / (Initial_Cost + 3yr_Power_Cost + 3yr_Maintenance_Cost)。其中 Quality_Score 需归一化至 0-1 区间（基于 MMLU/HumanEval 相对 BF16 的保留率），以量化精度损失对有效性能的影响，避免单纯追求高吞吐而忽视输出质量不可接受的情况。

## Evidence

检索失败: no sources from any channel (all 5 failed)
