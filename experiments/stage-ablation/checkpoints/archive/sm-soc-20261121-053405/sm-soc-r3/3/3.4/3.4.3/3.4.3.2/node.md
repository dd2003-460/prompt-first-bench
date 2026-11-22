# N165: 弹性系数 β_trust 的异质性分解：β_trust 并非单一常数，而是随用户生命周期阶段变化的函数 β_trust(LTV_stage)。新客阶段 β_tr

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

弹性系数 β_trust 的异质性分解：β_trust 并非单一常数，而是随用户生命周期阶段变化的函数 β_trust(LTV_stage)。新客阶段 β_trust_new ≈ 1.2（信任建立初期敏感度高），老客阶段 β_trust_old ≈ 0.3（边际效用递减）。由于平台用户中老客占比通常 >60%，加权平均 β_trust ≈ 0.5-0.7，低于父节点给出的上限 1.5，因此长期 GMV 增长预测应保守估计。

## Corrected Claim

弹性系数 β_trust 具有异质性，通常随用户生命周期阶段变化（新客阶段敏感度高于老客阶段）。由于多数成熟平台老客占比较高，加权平均 β_trust 往往低于新客阶段的峰值，因此长期 GMV 增长预测应考虑这种边际效用递减效应，采取保守估计。

## Evidence

[质询]数值量级与具体参数缺乏实证支持：β_trust_new ≈ 1.2 和 β_trust_old ≈ 0.3 是具体的经验参数，无法从第一性原理推导，且‘老客占比>60%’也是特定平台的经验数据，不同平台差异巨大，直接断言加权平均为0.5-0.7缺乏普适性依据。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体弹性系数数值属于经验参数，不适用第一性原理推导条款）

## Search Query

customer lifetime value trust elasticity heterogeneity marketplace
