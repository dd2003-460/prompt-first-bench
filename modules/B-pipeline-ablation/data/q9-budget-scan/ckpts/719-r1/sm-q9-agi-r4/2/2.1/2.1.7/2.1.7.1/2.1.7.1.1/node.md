# N464: 工作点 A (低成本/高噪声)：权重 w=[0.2, 0.2, 0.2, 0.2, 0.2]，评分者仅 1 人 (LLM-as-Judge GPT-4o, te

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N164

## Claim

工作点 A (低成本/高噪声)：权重 w=[0.2, 0.2, 0.2, 0.2, 0.2]，评分者仅 1 人 (LLM-as-Judge GPT-4o, temp=0.0)，单次评分成本 C_Rubric ≈ $0.02 (基于 1k tokens 输入+500 输出)，信噪比 SNR 较低，预期与人类专家 Pearson r ≈ 0.65 [待核验]

## Corrected Claim

工作点 A (低成本/高噪声)：权重 w=[0.2, 0.2, 0.2, 0.2, 0.2]，评分者仅 1 人 (LLM-as-Judge GPT-4o, temp=0.0)，单次评分成本较低（估算约 $0.02 量级），信噪比 SNR 较低，预期与人类专家相关性中等（Pearson r 可能在 0.6-0.7 区间，具体数值需实证验证）。

## Evidence

[质询]该陈述包含具体的经验参数（GPT-4o 特定 token 数下的成本 $0.02、特定配置下与人类专家的 Pearson r ≈ 0.65），这些数值并非第一性原理可推导，且缺乏当前检索来源的直接支持或验证。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体成本与相关性数值）

## Search Query

LLM as judge reliability Pearson correlation human experts scientific evaluation cost per call GPT-4o
