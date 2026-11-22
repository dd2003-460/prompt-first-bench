# N269: 用户流失率对价格透明化的敏感度函数 $\lambda_{churn}(C_{comp})$：建模为 $\lambda_{churn} = \alpha \cdo

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N89

## Claim

用户流失率对价格透明化的敏感度函数 $\lambda_{churn}(C_{comp})$：建模为 $\lambda_{churn} = \alpha \cdot (1 - HHI)^{\beta}$ 或类似非线性形式。需确定参数 $\alpha$（最大潜在流失率）和 $\beta$（竞争弹性）。若 HHI 低（竞争激烈），$\lambda_{churn}$ 对 $P_{ref}$ 显示的响应更陡峭；若 HHI 高，$\lambda_{churn} \approx 0$。

## Corrected Claim

用户流失率对价格透明化的敏感度函数 $\lambda_{churn}(C_{comp})$：建模为 $\lambda_{churn} = \alpha \cdot (1 - HHI)^{\beta}$ 或类似非线性形式。需确定参数 $\alpha$（最大潜在流失率）和 $\beta$（竞争弹性）。若 HHI 低（竞争激烈），$\lambda_{churn}$ 对 $P_{ref}$ 显示的响应更陡峭；若 HHI 高，$\lambda_{churn} \approx 0$。

## Evidence

先验知识/题面给定，逻辑校验通过：HHI（赫芬达尔-赫希曼指数）是衡量市场集中度的标准指标，HHI越低代表竞争越激烈，通常伴随更高的用户转换率和流失敏感度；该建模假设符合微观经济学中关于竞争加剧导致价格敏感度上升的基本直觉，且作为模型设定（而非经验事实断言），其逻辑自洽性成立。
