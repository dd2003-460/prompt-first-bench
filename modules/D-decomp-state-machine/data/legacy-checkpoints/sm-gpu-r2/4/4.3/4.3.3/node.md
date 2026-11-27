# N66: 散热环境对有效功耗系数的修正公式：Effective_Power_W = P_actual * (1 + Cooling_Overhead_Factor)，其中

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N18

## Claim

散热环境对有效功耗系数的修正公式：Effective_Power_W = P_actual * (1 + Cooling_Overhead_Factor)，其中 Cooling_Overhead_Factor 对于风冷工作站为 0.1-0.15（风扇能耗），对于水冷为 0.05-0.08（水泵能耗），对于数据中心 SXM 模块为 0（已包含在 PSU 效率中）。此系数需乘以 P_actual 后用于年电费计算。

## Corrected Claim

散热环境对有效功耗系数的修正公式：Effective_Power_W = P_actual * (1 + Cooling_Overhead_Factor)，其中 Cooling_Overhead_Factor 为经验估算值，风冷工作站约为 0.05-0.15，水冷约为 0.02-0.08，数据中心 SXM 模块散热能耗通常单独计算或包含在整体 PUE 中，不直接叠加于 GPU 功耗。

## Evidence

[质询]该公式将散热能耗（风扇/水泵）简单线性叠加到GPU实际功耗上，忽略了散热系统能耗通常与负载非线性相关且占比极小（通常<5%），0.1-0.15的系数对于风冷工作站而言量级偏大，且数据中心SXM模块散热能耗并非严格为0（液冷泵/CDU能耗独立于PSU效率），属于经验性工程估算而非严格物理定律。 | source=knowledge，逻辑自洽但缺乏外部来源直接支持具体数值范围，且经验参数存在工程简化假设，依据经验事实排除条款降级。
