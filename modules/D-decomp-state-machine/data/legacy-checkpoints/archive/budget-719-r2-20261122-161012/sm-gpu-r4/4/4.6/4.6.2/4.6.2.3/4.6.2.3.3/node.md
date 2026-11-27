# N590: 故障停机损失 (Downtime_Loss) 的期望值计算：E[Downtime_Loss] = (1/MTBF) * MTTR * Hourly_Revenu

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N245

## Claim

故障停机损失 (Downtime_Loss) 的期望值计算：E[Downtime_Loss] = (1/MTBF) * MTTR * Hourly_Revenue_Loss；H100 数据中心卡 MTBF 约为 50,000-100,000 小时，MTTR (平均修复时间) 约为 4-8 小时（需专业人员上门）；若每小时机会成本为 $500 (基于 $10k/月 工程师薪资 + 业务停滞损失)，则年期望停机损失 = (1/75,000) * 6h * $500/h * 8760h ≈ $350/年。此数值低于 N245 中 $500-$1000 的保守估算，但需加上备件等待时间导致的额外停机。

## Corrected Claim

故障停机损失 (Downtime_Loss) 的期望值计算：E[Downtime_Loss] = (1/MTBF) * MTTR * Hourly_Revenue_Loss；H100 数据中心卡 MTBF 约为 50,000-100,000 小时，MTTR (平均修复时间) 约为 4-8 小时（需专业人员上门）；若每小时机会成本为 $500 (基于 $10k/月 工程师薪资 + 业务停滞损失)，则年期望停机损失 = (1/75,000) * 6h * $500/h * 8760h ≈ $350/年。此数值低于 N245 中 $500-$1000 的保守估算，但需加上备件等待时间导致的额外停机。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 E[Loss] = (1/MTBF)*MTTR*Cost 量纲正确；数值计算 (1/75000)*6*500*8760 ≈ 350.4 准确；H100 MTBF (50k-100k h) 和 MTTR (4-8 h) 符合数据中心硬件工程常识。
