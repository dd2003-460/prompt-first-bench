# N86: 针对动态内容（如新闻/社交信息流），实证研究显示更新率可达 5%-10%/天，此时 P_invalid ≈ 0.05-0.1 * T_resident，若 T_

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N25

## Claim

针对动态内容（如新闻/社交信息流），实证研究显示更新率可达 5%-10%/天，此时 P_invalid ≈ 0.05-0.1 * T_resident，若 T_resident=1 天，折损因子降至 0.9-0.95，显著影响命中率；该数据来自 Facebook 2016 年数据基础设施论文，属于'刚查到的'特定场景数据。

## Corrected Claim

针对动态内容（如新闻/社交信息流），实证研究显示更新率可能较高（例如 5%-10%/天），此时若 T_resident=1 天，折损因子可能降至 0.9-0.95，显著影响命中率；具体数值需参考相关实证研究（如 Facebook 等大厂的数据基础设施论文）。

## Evidence

[质询]该陈述包含具体的经验数据（5%-10%/天更新率）和特定来源归属（Facebook 2016 论文），属于经验事实。由于检索失败，无法验证该具体数值是否真实出自该论文，也无法排除其他研究得出的不同更新率范围，存在来源不可靠或数据张冠李戴的风险。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无法验证具体数值及来源归属）

## Search Query

Facebook data infrastructure dynamic content update rate percentage per day
