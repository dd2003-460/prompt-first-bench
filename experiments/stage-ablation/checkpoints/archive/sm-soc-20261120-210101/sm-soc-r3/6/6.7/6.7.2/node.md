# N371: 高信用卖家的阈值定义：'高信用' 定义为 μ_credit > μ_credit_category + 1.0 * σ_credit_category，其中 μ

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N109

## Claim

高信用卖家的阈值定义：'高信用' 定义为 μ_credit > μ_credit_category + 1.0 * σ_credit_category，其中 μ_credit_category 为品类平均信用分，σ_credit_category 为品类信用分标准差；若未定义阈值，检验无效。

## Corrected Claim

高信用卖家的阈值定义通常基于品类信用分的统计分布（如均值加若干倍标准差），具体阈值（如1.0σ）需依据特定业务规则或模型设定确定，若无明确定义则检验无效。

## Evidence

[质询]该陈述定义了一个具体的统计阈值（均值+1.0标准差），属于经验性参数设定或特定业务规则，无法从第一性原理或数学公理中严格推导得出。不同的风控模型或业务场景可能采用不同的阈值（如1.5σ, 2σ或固定分数），因此该具体数值缺乏普适性的逻辑必然性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该阈值非数学恒等式，属业务定义范畴）

## Search Query

threshold definition for high credit seller in e-commerce
