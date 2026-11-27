# N206: 折现率 r 的选取：r 应反映平台资金成本或机会成本，通常取 5%-10% 年化。若 r 取值过高，长期 GMV 损失被低估；若 r 取值过低，短期损失被高估。

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N66

## Claim

折现率 r 的选取：r 应反映平台资金成本或机会成本，通常取 5%-10% 年化。若 r 取值过高，长期 GMV 损失被低估；若 r 取值过低，短期损失被高估。需量化 r 对 ΔGMV 总体的敏感性：ΔGMV(r=5%) vs ΔGMV(r=10%) 的差异若 > 20%，则结论对 r 高度敏感，需明确 r 的取值依据。

## Corrected Claim

折现率 r 的选取：r 应反映平台资金成本或机会成本，通常取 5%-10% 年化。若 r 取值过高，长期 GMV 损失被低估；若 r 取值过低，短期损失被高估。需量化 r 对 ΔGMV 总体的敏感性：ΔGMV(r=5%) vs ΔGMV(r=10%) 的差异若 > 20%，则结论对 r 高度敏感，需明确 r 的取值依据。

## Evidence

先验知识/题面给定，逻辑校验通过：折现率反映资金/机会成本，5%-10%为常见区间；r升高导致远期现金流现值降低，故长期损失被低估，短期损失相对权重增加（高估），逻辑自洽。

## Search Query

discount rate selection GMV loss calculation e-commerce platform
