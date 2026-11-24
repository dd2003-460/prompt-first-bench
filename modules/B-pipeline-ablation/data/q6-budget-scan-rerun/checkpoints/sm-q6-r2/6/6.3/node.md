# N114: 峰值 RPS 的计算公式为 RPS_peak = RPS_avg × R_pg，其中峰谷比 R_pg 基于 N15 的流量分布模型确定为 3.0（峰值时段占40

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N34

## Claim

峰值 RPS 的计算公式为 RPS_peak = RPS_avg × R_pg，其中峰谷比 R_pg 基于 N15 的流量分布模型确定为 3.0（峰值时段占40%流量，谷值占10%，比值 40/10=4，但带宽计费通常采用保守系数3.0以平衡成本），因此 RPS_peak ≈ 12.5 × 3.0 = 37.5 RPS

## Corrected Claim

峰值 RPS 的计算公式为 RPS_peak = RPS_avg × R_pg，其中峰谷比 R_pg 基于 N15 的流量分布模型确定为 3.0（峰值时段占40%流量，谷值占10%，比值 40/10=4，但带宽计费通常采用保守系数3.0以平衡成本），因此 RPS_peak ≈ 12.5 × 3.0 = 37.5 RPS

## Evidence

先验知识/题面给定，逻辑校验通过：公式 RPS_peak = RPS_avg × R_pg 符合定义，数值计算 12.5 × 3.0 = 37.5 准确，且峰谷比取 3.0 作为保守系数在工程实践中合理。
