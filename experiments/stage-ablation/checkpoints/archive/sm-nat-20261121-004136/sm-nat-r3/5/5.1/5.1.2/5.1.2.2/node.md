# N146: LFU 频率遗忘率 λ_forget 的量化约束：在更新率 λ_update=0.01/day 下，为使 LFU 计数器能反映最新热度，λ_forget 必须满

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N61

## Claim

LFU 频率遗忘率 λ_forget 的量化约束：在更新率 λ_update=0.01/day 下，为使 LFU 计数器能反映最新热度，λ_forget 必须满足 λ_forget * T_window ≥ 1/λ_update，即 T_window ≤ 100 days。若 T_window 取 1 天（日级统计），则 λ_forget = 1.0 day^-1。

## Corrected Claim

在更新率 λ_update=0.01/day 下，若设定遗忘率 λ_forget = 1.0 day^-1，则窗口期 T_window 应满足 T_window ≤ 1/λ_update = 100 days 以确保计数器反映最新热度。若 T_window 取 1 天，则 λ_forget 需至少为 1.0 day^-1 才能满足该约束（假设约束为 λ_forget * T_window ≥ 1/λ_update）。

## Evidence

[质询]公式推导存在逻辑跳跃：从 λ_forget * T_window ≥ 1/λ_update 推导出 T_window ≤ 100 days 在数学上不成立（若 λ_forget 是变量，T_window 的上界依赖于 λ_forget 的具体值，而非固定为 100；若 λ_forget 固定为 1，则 T_window ≤ 100 成立，但前文未固定 λ_forget）。此外，'1/λ_update' 作为时间常数的物理意义（即平均更新间隔）与 'λ_forget * T_window' 的量纲（无量纲）直接比较缺乏明确的物理模型支撑，属于经验性启发式规则而非严格推导。 | 先验知识/题面给定，但逻辑校验发现不等式推导存在变量依赖错误，且经验事实缺乏来源支持，故降级。
