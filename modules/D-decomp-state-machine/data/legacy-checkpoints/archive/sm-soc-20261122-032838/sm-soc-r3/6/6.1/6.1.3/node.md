# N282: P_re-search,base的时间窗口敏感性：48h内P_re-search,base ≈ 50-60%，72h内P_re-search,base ≈ 30

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N93

## Claim

P_re-search,base的时间窗口敏感性：48h内P_re-search,base ≈ 50-60%，72h内P_re-search,base ≈ 30-40%，需明确测量时间窗口以匹配'48h无咨询'的观察

## Corrected Claim

P_re-search,base随时间窗口增加而显著下降（如48h内高于72h内），需明确测量时间窗口以匹配'48h无咨询'的观察。

## Evidence

[质询]具体数值区间（50-60% vs 30-40%）缺乏通用理论或标准基准支持，属于特定场景下的经验估计，不同业务场景下波动极大，无法从第一性原理严格推导。 | 逻辑自洽（时间窗口越长，重新搜索概率越低符合直觉），但具体数值为经验事实，无来源支持且非第一性原理可推导，故降级。
