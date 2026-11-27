# N269: 未成交占比动态监测公式：p_unsold(t) = N_unsold(t) / N_total(t)，其中 N_unsold(t) 为第 t 天未成交商品数；需

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N91

## Claim

未成交占比动态监测公式：p_unsold(t) = N_unsold(t) / N_total(t)，其中 N_unsold(t) 为第 t 天未成交商品数；需计算 p_unsold(t) 的时间序列，若任意时刻 p_unsold(t) > 0.3，则触发标准误放大机制，否则使用原始 SE。

## Corrected Claim

未成交占比动态监测公式：p_unsold(t) = N_unsold(t) / N_total(t)，其中 N_unsold(t) 为第 t 天未成交商品数；需计算 p_unsold(t) 的时间序列，若任意时刻 p_unsold(t) > 0.3，则触发标准误放大机制，否则使用原始 SE。

## Evidence

先验知识/题面给定，逻辑校验通过
