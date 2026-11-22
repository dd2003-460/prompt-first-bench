# N30: 下游投影：挂价溢价率 P_markup 中的噪声贡献项，计算公式为 P_markup_noise = k * σ²_pref，其中 k 为风险规避系数，需通过回

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N5, N6, N7

## Claim

下游投影：挂价溢价率 P_markup 中的噪声贡献项，计算公式为 P_markup_noise = k * σ²_pref，其中 k 为风险规避系数，需通过回归分析确定 k 的具体数值，预期 k 在 0.1-0.3 之间。

## Corrected Claim

下游投影：挂价溢价率 P_markup 中的噪声贡献项，计算公式为 P_markup_noise = k * σ²_pref，其中 k 为风险规避系数，需通过回归分析确定 k 的具体数值。

## Evidence

[质询]该陈述包含具体的经验参数（k 的预期范围 0.1-0.3）和特定的模型结构假设，属于经验事实而非第一性原理可推导的数学或逻辑恒等式。在缺乏外部来源支持的情况下，无法验证 k 的具体数值范围是否准确，也无法确认该线性噪声贡献模型是否为该领域公认的标准形式。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且 k 的具体数值范围属于经验参数，不适用第一性原理推导条款）

## Search Query

risk aversion coefficient k regression markup preference noise
