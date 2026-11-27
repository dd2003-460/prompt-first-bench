# N231: η_speed（速度提升系数）的分解：η_speed = η_info * P(ReadLabel) + η_match * ΔFriction，其中 η_in

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

η_speed（速度提升系数）的分解：η_speed = η_info * P(ReadLabel) + η_match * ΔFriction，其中 η_info 为信息透明度对搜索效率的提升（估计 0.05-0.08），η_match 为匹配效率提升（估计 0.02-0.05）；两项之和需通过 A/B 测试中的处理组与控制组 T_close 差异分解得出。

## Corrected Claim

η_speed（速度提升系数）的分解：η_speed = η_info * P(ReadLabel) + η_match * ΔFriction，其中 η_info 为信息透明度对搜索效率的提升（估计 0.05-0.08），η_match 为匹配效率提升（估计 0.02-0.05）；两项之和需通过 A/B 测试中的处理组与控制组 T_close 差异分解得出。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

A/B test decomposition speedup coefficient information transparency matching efficiency
