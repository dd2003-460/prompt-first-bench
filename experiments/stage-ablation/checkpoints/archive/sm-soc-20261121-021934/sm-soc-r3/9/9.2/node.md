# N137: 成交率下降幅度 Drop_Rate 的精确计算定义为 Drop_Rate = (CR_base - CR_current) / CR_base，其中 CR_ba

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N58

## Claim

成交率下降幅度 Drop_Rate 的精确计算定义为 Drop_Rate = (CR_base - CR_current) / CR_base，其中 CR_base 为过去 30 天同类商品基准成交率，CR_current 为最近 7 天成交率；需排除季节性因素，通过差分法 ΔDrop_Rate = Drop_Rate_t - Drop_Rate_{t-1} 剔除趋势项，以准确识别由市场供给增加导致的真实稀缺信号。

## Corrected Claim

成交率下降幅度 Drop_Rate 的精确计算定义为 Drop_Rate = (CR_base - CR_current) / CR_base，其中 CR_base 为过去 30 天同类商品基准成交率，CR_current 为最近 7 天成交率；需排除季节性因素，通过差分法 ΔDrop_Rate = Drop_Rate_t - Drop_Rate_{t-1} 剔除趋势项，以准确识别由市场供给增加导致的真实稀缺信号。

## Evidence

先验知识/题面给定，逻辑校验通过
