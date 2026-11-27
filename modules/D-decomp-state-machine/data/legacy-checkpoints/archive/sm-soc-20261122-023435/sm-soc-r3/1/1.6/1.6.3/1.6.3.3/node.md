# N129: 均衡稳定性的利润差计算：ΔProfit = (P_high - C_cost) * Q_high - (P_low - C_cost) * Q_low，其中 Q

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42

## Claim

均衡稳定性的利润差计算：ΔProfit = (P_high - C_cost) * Q_high - (P_low - C_cost) * Q_low，其中 Q_high = Q_base * E_high * CTR_high，Q_low = Q_base * E_low * CTR_low。需代入 N40-N42 的公式，计算卖家维持高价 vs 降价的期望利润差，验证纳什均衡条件 ΔProfit > 0。

## Corrected Claim

均衡稳定性的利润差计算：ΔProfit = (P_high - C_cost) * Q_high - (P_low - C_cost) * Q_low，其中 Q_high = Q_base * E_high * CTR_high，Q_low = Q_base * E_low * CTR_low。需代入 N40-N42 的公式，计算卖家维持高价 vs 降价的期望利润差，验证纳什均衡条件 ΔProfit > 0。

## Evidence

先验知识/题面给定，逻辑校验通过：利润差公式符合基本经济学定义（(价格-成本)*数量），且纳什均衡条件（维持高价利润大于降价利润）逻辑自洽。
