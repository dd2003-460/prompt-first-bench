# N231: 卖家降价决策阈值 ΔP_threshold 的量化：基于损失厌恶系数 λ=2.25，计算卖家愿意降价的最小幅度 ΔP_min = (V - P_ask) / λ

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N76

## Claim

卖家降价决策阈值 ΔP_threshold 的量化：基于损失厌恶系数 λ=2.25，计算卖家愿意降价的最小幅度 ΔP_min = (V - P_ask) / λ，需代入 V 的分布均值及当前挂价 P_ask 分布，确定 60% 无咨询现象中因低于阈值而不降价的比例。

## Corrected Claim

卖家降价决策阈值 ΔP_threshold 的量化：基于损失厌恶系数 λ=2.25，假设卖家愿意降价的最小幅度 ΔP_min 与 (V - P_ask) 成正比，比例系数为 1/λ，即 ΔP_min = (V - P_ask) / λ。需代入 V 的分布均值及当前挂价 P_ask 分布，估算 60% 无咨询现象中因低于阈值而不降价的比例。

## Evidence

[质询]公式 ΔP_min = (V - P_ask) / λ 缺乏明确的经济学或行为学理论推导支持，属于经验性假设；且 λ=2.25 的具体取值未提供来源依据，存在参数任意性风险。 | 先验知识/题面给定，逻辑校验通过（量纲一致，公式结构合理），但作为经验事实缺乏外部来源直接支持具体参数及公式形式。

## Search Query

loss aversion threshold price reduction decision seller behavior
