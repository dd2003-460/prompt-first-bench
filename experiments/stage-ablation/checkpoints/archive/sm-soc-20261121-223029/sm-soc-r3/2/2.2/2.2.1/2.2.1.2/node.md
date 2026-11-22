# N168: 在降价幅度 5% <= |ΔP|/P_ask <= 15% 的触发区间，P(Lemon | ΔP < 0) 跃升至 0.6-0.8，导致咨询意愿 C_inqui

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N50

## Claim

在降价幅度 5% <= |ΔP|/P_ask <= 15% 的触发区间，P(Lemon | ΔP < 0) 跃升至 0.6-0.8，导致咨询意愿 C_inquiry 下降至 C_base * e^(-0.7 * λ_lemon)，若 λ_lemon > 1.5，则 C_inquiry 将低于平台通知阈值 Threshold_notification，造成 60% 卖家无咨询的现象。

## Corrected Claim

在降价幅度 5% <= |ΔP|/P_ask <= 15% 的触发区间，P(Lemon | ΔP < 0) 显著上升，导致咨询意愿 C_inquiry 下降；若柠檬风险厌恶参数 λ_lemon 超过特定阈值，C_inquiry 将低于平台通知阈值，造成部分卖家无咨询的现象。

## Evidence

[质询]该陈述包含大量未定义的具体经验参数（如概率跃升至0.6-0.8、指数系数0.7、阈值λ_lemon>1.5、60%卖家无咨询），这些数值缺乏理论推导基础或实证数据支持，属于典型的经验事实断言，无法从第一性原理严格推出。 | 经验事实，逻辑自洽但缺来源支持
