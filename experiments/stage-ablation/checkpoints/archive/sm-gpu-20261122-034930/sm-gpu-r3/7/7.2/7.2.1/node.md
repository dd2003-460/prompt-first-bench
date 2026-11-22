# N392: AMD MI300X 基础设施成本工作点1（最低可行配置/高性低成）：采用单路EPYC服务器（如Supermicro AS-2115GS-TNR）+ 2x 16

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N140

## Claim

AMD MI300X 基础设施成本工作点1（最低可行配置/高性低成）：采用单路EPYC服务器（如Supermicro AS-2115GS-TNR）+ 2x 1600W 80+ Titanium电源 + 被动风冷/基本风冷，硬件总成本（不含GPU）约为 $3,500（服务器$2,000 + 电源$500 + 机箱/线缆$1,000），这是满足750W TDP和冗余电源要求的最小物理边界。

## Corrected Claim

AMD MI300X 基础设施成本工作点1（最低可行配置/高性低成）：采用单路EPYC服务器 + 2x 1600W 80+ Titanium电源 + 被动风冷/基本风冷，硬件总成本（不含GPU）约为 $3,500（服务器$2,000 + 电源$500 + 机箱/线缆$1,000），这是满足750W TDP和冗余电源要求的最小物理边界。

## Evidence

[质询]硬件成本属于经验事实，且具体型号（Supermicro AS-2115GS-TNR）与MI300X的兼容性存疑（该型号通常支持EPYC 9004系列，而MI300X通常搭配EPYC 9005系列或特定OEM服务器），且$3,500的硬件成本估算缺乏实时市场数据支持，可能低估了高端服务器组件的价格。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Supermicro AS-2115GS-TNR price 2024
