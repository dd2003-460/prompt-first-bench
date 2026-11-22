# N833: 2x RTX 4090 方案的总功耗为 2 * 450W (TDP) = 900W，但实际推理平均功耗约为 2 * 380W = 760W（基于 TechPow

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N260

## Claim

2x RTX 4090 方案的总功耗为 2 * 450W (TDP) = 900W，但实际推理平均功耗约为 2 * 380W = 760W（基于 TechPowerUp 实测 [search]），导致年 OpEx 从 $7,884 修正为约 $6,655。

## Corrected Claim

2x RTX 4090 方案的总功耗为 2 * 450W (TDP) = 900W，实际推理平均功耗通常低于TDP（具体数值需实测确认），导致年 OpEx 低于基于TDP计算的 $7,884。

## Evidence

[质询]具体数值（380W平均功耗、$6,655年OpEx）属于经验事实，且参考来源缺失，无法验证TechPowerUp实测数据的准确性及OpEx计算的具体电价/负载假设。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

RTX 4090 average power consumption LLM inference watts measured
