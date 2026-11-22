# N246: RTX 4080 在持续 LLM 推理负载下的实际平均功耗 (P_avg) 实测值，通常低于 320W TDP，需引用特定基准测试数据以精确计算能效比和 OpE

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N66

## Claim

RTX 4080 在持续 LLM 推理负载下的实际平均功耗 (P_avg) 实测值，通常低于 320W TDP，需引用特定基准测试数据以精确计算能效比和 OpEx_energy [待核验：需检索实测功耗数据]

## Corrected Claim

RTX 4080 在持续 LLM 推理负载下的实际平均功耗 (P_avg) 通常低于其 320W TDP 上限，具体数值需依据特定基准测试数据确定。

## Evidence

[质询]该陈述包含具体的经验性数值断言（'通常低于 320W'），属于硬件功耗规格/实测数据，无法从第一性原理推导，且缺乏来源支持以确认其普遍性或具体基准测试条件。 | 经验事实，逻辑自洽（RTX 4080 TDP为320W，持续负载下平均功耗通常低于峰值TDP符合物理直觉），但检索无可用来源，无法提供直接支持或排除特定高负载场景下接近TDP的可能性。

## Search Query

RTX 4080 average power consumption LLM inference benchmark
