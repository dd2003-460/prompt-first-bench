# N239: R_relist 的分子'修改价格次数'需区分'微调'（ΔP < 1%）与'显著调整'（ΔP ≥ 1%），仅显著调整计入 Price Probing；若包含微调

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N65

## Claim

R_relist 的分子'修改价格次数'需区分'微调'（ΔP < 1%）与'显著调整'（ΔP ≥ 1%），仅显著调整计入 Price Probing；若包含微调，R_relist 虚高约 30-50%，因为卖家常进行无实质影响的界面刷新或小数位调整。量化修正：R_relist_adj = Count[ΔP ≥ 1%] / Total_Drops。

## Corrected Claim

R_relist 的分子'修改价格次数'需区分'微调'（ΔP < 1%）与'显著调整'（ΔP ≥ 1%），仅显著调整计入 Price Probing；若包含微调，R_relist 可能会虚高（具体幅度依市场而定，常见估计在 30-50% 左右），量化修正公式为：R_relist_adj = Count[ΔP ≥ 1%] / Total_Drops。

## Evidence

[质询]「R_relist 虚高约 30-50%」是一个具体的经验统计数值，缺乏普遍适用的理论依据或广泛认可的基准数据支持，不同市场、品类或平台的数据可能差异巨大，该具体百分比可能不准确或仅适用于特定未指明的数据集。 | source=knowledge，逻辑自洽（区分微调与显著调整在方法论上合理），但「30-50%」的具体量化修正系数属于经验事实，无来源支持且无法从第一性原理严格推出，故降级。
