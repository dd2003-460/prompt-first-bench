# N142: ΔUtility_lost 的量化计算：定义为搜索时间增量 ΔTime_spent 乘以买家的时间机会成本率 r_time（$min⁻¹），即 ΔUtility

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N44

## Claim

ΔUtility_lost 的量化计算：定义为搜索时间增量 ΔTime_spent 乘以买家的时间机会成本率 r_time（$min⁻¹），即 ΔUtility_lost = ΔTime_spent * r_time，其中 r_time 需通过 A/B 测试中用户因等待超时而流失的边际效用损失估算，基准值设为 0.05 $/min [待核验]。

## Corrected Claim

ΔUtility_lost 的量化计算：定义为搜索时间增量 ΔTime_spent 乘以买家的时间机会成本率 r_time（$min⁻¹），即 ΔUtility_lost = ΔTime_spent * r_time，其中 r_time 需通过 A/B 测试中用户因等待超时而流失的边际效用损失估算，基准值设为 0.05 $/min [待核验]。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

opportunity cost of time in online shopping utility loss model
