# N204: w_2 (PriceReasonableness权重) 的敏感性分析：需计算 ∂Score/∂w_2 对整体成交率 CVR 的影响。若 w_2 从 0 增加至 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N65

## Claim

w_2 (PriceReasonableness权重) 的敏感性分析：需计算 ∂Score/∂w_2 对整体成交率 CVR 的影响。若 w_2 从 0 增加至 0.2，需验证 CVR 是否显著提升。若 CVR 提升幅度 < 5%，则说明买家对价格合理性不敏感，w_2 应维持低位，这与题面'高溢价快速成交'现象一致。

## Corrected Claim

w_2 (PriceReasonableness权重) 的敏感性分析：需计算 ∂Score/∂w_2 对整体成交率 CVR 的影响。若 w_2 从 0 增加至 0.2，需验证 CVR 是否显著提升。若 CVR 提升幅度 < 5%，则说明买家对价格合理性不敏感，w_2 应维持低位，这与题面'高溢价快速成交'现象一致。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

price reasonableness weight sensitivity analysis conversion rate
