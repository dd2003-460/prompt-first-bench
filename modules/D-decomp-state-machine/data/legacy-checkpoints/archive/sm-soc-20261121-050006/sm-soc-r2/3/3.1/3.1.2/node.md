# N69: 下游投影 1（卖家定价调整幅度）：卖家挂价下调幅度 ΔP_ask = -k_sens * (P_ask - P_median) * P(ReadLabel)，其

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N14

## Claim

下游投影 1（卖家定价调整幅度）：卖家挂价下调幅度 ΔP_ask = -k_sens * (P_ask - P_median) * P(ReadLabel)，其中 k_sens 为卖家对价格信号的敏感度（估计值 0.2-0.4），P(ReadLabel) 为买家阅读标签的概率；当 P(ReadLabel) < 0.5 时，ΔP_ask 趋近于 0，干预失效。

## Corrected Claim

下游投影 1（卖家定价调整幅度）：卖家挂价下调幅度 ΔP_ask = -k_sens * (P_ask - P_median) * P(ReadLabel)，其中 k_sens 为卖家对价格信号的敏感度（估计值 0.2-0.4），P(ReadLabel) 为买家阅读标签的概率；当 P(ReadLabel) < 0.5 时，ΔP_ask 趋近于 0，干预失效。

## Evidence

先验知识/题面给定，逻辑校验通过
