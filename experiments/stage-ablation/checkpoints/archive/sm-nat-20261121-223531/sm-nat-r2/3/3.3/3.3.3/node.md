# N51: LFU 工作点 2 相比工作点 1 的增益损失主要来源于频率估计滞后，量化为 ΔH_loss = ∫ (f_H_LFU(h,t) - f_H(h)) * E[S

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N15

## Claim

LFU 工作点 2 相比工作点 1 的增益损失主要来源于频率估计滞后，量化为 ΔH_loss = ∫ (f_H_LFU(h,t) - f_H(h)) * E[S|H=h] dh，在 λ=0.5/day 时，该损失约为 1-2 个百分点，具体值需通过模拟验证。

## Corrected Claim

LFU 工作点 2 相比工作点 1 的增益损失主要来源于频率估计滞后，其量化公式为 ΔH_loss = ∫ (f_H_LFU(h,t) - f_H(h)) * E[S|H=h] dh；在 λ=0.5/day 时，该损失的具体数值需通过模拟验证确定。

## Evidence

[质询]该陈述包含具体的经验性数值结论（1-2个百分点），且声称该值需通过模拟验证，属于经验事实而非第一性原理可推导的数学性质；在缺乏外部来源支持的情况下，无法确认该具体数值范围的准确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

LFU frequency estimation lag hit rate loss Pareto distribution
