# N74: 本地 Qwen3.8-27B 作为 Judge 的能力上限：在逻辑一致性任务上，其 Kappa 系数 κ_local ≈ 0.65-0.70，显著低于 GPT-

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N19, N20, N21

## Claim

本地 Qwen3.8-27B 作为 Judge 的能力上限：在逻辑一致性任务上，其 Kappa 系数 κ_local ≈ 0.65-0.70，显著低于 GPT-4o-mini 的 0.80-0.85；主要偏差来源于对隐含前提的识别不足（Missed Implicit Premises），导致 D1 维度得分系统性偏高 0.1-0.15；若必须使用本地 Judge，需增加人工抽查比例至 30%（从 20% 提升），以补偿 0.1 的 Kappa 差距带来的误判率上升。

## Corrected Claim

本地 Qwen3.8-27B 作为 Judge 在逻辑一致性任务上的表现通常弱于 GPT-4o-mini，主要偏差源于对隐含前提识别不足，导致 D1 维度得分系统性偏高。若必须使用本地 Judge，建议适当提高人工抽查比例以补偿潜在的误判率上升。

## Evidence

[质询]该陈述包含大量具体的经验性数值（Kappa系数区间、偏差幅度、人工抽查比例调整），这些并非逻辑或数学上的必然结论，而是依赖于特定数据集、评估协议和模型版本的实证结果。作为knowledge节点，虽然允许基于先验知识判定，但如此精确且具体的对比数据（特别是GPT-4o-mini的具体Kappa值及两者间的量化差距）缺乏通用的公认基准支持，存在将特定实验结果泛化为普遍真理的风险。 | 先验知识/题面给定，逻辑校验通过（逻辑链条自洽：Kappa降低->误判率上升->需增加人工抽查），但具体数值属于特定场景下的经验估计，非普适常数，故降级为定性表述。

## Search Query

local LLM judge kappa coefficient bias implicit premise detection gap vs GPT-4o
