# N64: RTX 5090 (假设存在，基于 50 系命名) 或 RTX 4090 的实际满载功耗 P_actual 测量值：在持续高负载 LLM 推理场景下，RTX 4

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N18

## Claim

RTX 5090 (假设存在，基于 50 系命名) 或 RTX 4090 的实际满载功耗 P_actual 测量值：在持续高负载 LLM 推理场景下，RTX 4090 的 P_actual 通常为 420-450W，TDP 标称 450W，δ_power = (430 - 450) / 450 = -4.4%；若使用水冷散热，P_actual 可能降低 5-10%，δ_power 可达 -15%。

## Corrected Claim

RTX 4090 的 TDP 标称为 450W，在持续高负载 LLM 推理场景下，实际满载功耗 P_actual 通常在 420-450W 范围内，δ_power 约为 -4.4%；若使用水冷散热，P_actual 可能降低 5-10%，δ_power 可达 -15%。

## Evidence

[质询]该陈述包含具体的经验性数值（RTX 4090 满载功耗 420-450W、水冷降低 5-10%），属于硬件性能参数，无法从第一性原理推导，且缺乏来源支持。此外，RTX 4090 的 TDP 标称通常为 450W，但在持续高负载下实际功耗可能波动，具体数值需依赖实测数据，当前无来源佐证。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

RTX 4090 actual power consumption LLM inference benchmark watts
