# N389: RTX 4090在INT8 Decode阶段的实测功耗修正：基于TechPowerUp和GPU-DB的实测数据，RTX 4090在纯Decode负载（batch

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N152

## Claim

RTX 4090在INT8 Decode阶段的实测功耗修正：基于TechPowerUp和GPU-DB的实测数据，RTX 4090在纯Decode负载（batch=1, 32K context）下，GPU功耗约为320-350W（TDP 450W的71-78%），而非N152假设的60-70%；整机功耗（含CPU、内存、风扇）约为400-420W。

## Corrected Claim

RTX 4090在INT8 Decode阶段的实测功耗通常低于其450W TDP，具体数值需依据特定测试环境确定，但普遍高于60-70%的假设值。

## Evidence

[质询]具体数值（320-350W）属于经验事实，且缺乏本轮检索来源的直接支持，无法排除不同测试环境或驱动版本导致的偏差。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

RTX 4090 power consumption LLM inference decode phase watts measured TechPowerUp
