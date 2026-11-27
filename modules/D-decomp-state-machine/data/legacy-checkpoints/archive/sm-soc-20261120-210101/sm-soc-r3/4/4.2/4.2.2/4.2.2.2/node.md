# N279: V_time 的收入分层折算公式：V_time = (Hourly_Wage / 60) * η_sub，其中 η_sub 为时间替代系数（假设 0.5，即用户

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N77

## Claim

V_time 的收入分层折算公式：V_time = (Hourly_Wage / 60) * η_sub，其中 η_sub 为时间替代系数（假设 0.5，即用户只愿意支付时薪的一半作为机会成本）。低收入组（时薪<30元）V_time_low = 0.25元/分钟；高收入组（时薪>60元）V_time_high = 0.5元/分钟；需按用户收入分布加权计算平台整体 V_time。

## Corrected Claim

V_time 的收入分层折算公式：V_time = (Hourly_Wage / 60) * η_sub，其中 η_sub 为时间替代系数（假设 0.5，即用户只愿意支付时薪的一半作为机会成本）。低收入组（时薪<30元）V_time_low = 0.25元/分钟；高收入组（时薪>60元）V_time_high = 0.5元/分钟；需按用户收入分布加权计算平台整体 V_time。

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（元/小时 / 60 = 元/分钟），数值代入符合定义（30/60*0.5=0.25, 60/60*0.5=0.5），且作为模型假设自洽。

## Search Query

value of time income stratification consumer behavior e-commerce
