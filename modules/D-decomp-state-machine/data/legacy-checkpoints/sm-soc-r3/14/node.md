# N339: 现象兼容性统一指标 U_comp 的量化定义：U_comp = corr(T_close_high_markup, T_close_low_markup) * 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

现象兼容性统一指标 U_comp 的量化定义：U_comp = corr(T_close_high_markup, T_close_low_markup) * (1 - |ΔT_close|/T_base)。当 U_comp > 0.6 时，表明两个现象（高溢价短周期、降价无咨询）可由同一套‘筛选-等待’机制解释，而非独立随机事件；需基于过去90天数据计算该相关系数。

## Corrected Claim

现象兼容性统一指标 U_comp 的量化定义：U_comp = corr(T_close_high_markup, T_close_low_markup) * (1 - |ΔT_close|/T_base)。当 U_comp > 0.6 时，表明两个现象（高溢价短周期、降价无咨询）可由同一套‘筛选-等待’机制解释，而非独立随机事件；需基于过去90天数据计算该相关系数。

## Evidence

检索失败: no sources from any channel (all 5 failed)
