# N389: 用户混淆成本 C_user_confusion 的量化公式：C_user_confusion = ΔChurn * ARPU_monthly * N_activ

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N117

## Claim

用户混淆成本 C_user_confusion 的量化公式：C_user_confusion = ΔChurn * ARPU_monthly * N_active_users。其中 ΔChurn 为因信息过载导致的月流失率增加量，ARPU_monthly 为月均用户收入，N_active_users 为月活跃用户数。需通过 A/B 测试获取 ΔChurn 的估计值。

## Corrected Claim

用户混淆成本 C_user_confusion 的量化公式：C_user_confusion = ΔChurn * ARPU_monthly * N_active_users。其中 ΔChurn 为因信息过载导致的月流失率增加量，ARPU_monthly 为月均用户收入，N_active_users 为月活跃用户数。需通过 A/B 测试获取 ΔChurn 的估计值。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

information overload user churn rate online platform ARPU calculation
