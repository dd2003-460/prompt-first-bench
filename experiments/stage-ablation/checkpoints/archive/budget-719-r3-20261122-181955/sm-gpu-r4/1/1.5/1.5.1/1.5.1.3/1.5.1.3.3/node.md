# N576: Apple M3 Ultra 256GB 显存允许在 BF16 权重 (54GB) 下支持最大并发请求数 = (256 - 54 - 4) / 8 = 24 个

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N199

## Claim

Apple M3 Ultra 256GB 显存允许在 BF16 权重 (54GB) 下支持最大并发请求数 = (256 - 54 - 4) / 8 = 24 个请求 (扣除 4GB 系统开销)，而 M2 Ultra 192GB 仅支持 19 个请求，M3 Ultra 的并发容量优势显著高于其单请求吞吐优势。

## Corrected Claim

Apple M3 Ultra 256GB 显存相较于 M2 Ultra 192GB 显存，在相同模型权重和单请求显存占用假设下，理论上可支持更多的并发请求数，其并发容量优势显著。

## Evidence

[质询]该陈述包含具体的经验性参数假设（如每请求8GB显存占用、4GB系统开销、54GB模型权重），这些数值并非第一性原理可推导，且缺乏来源支持，属于经验事实。 | 经验事实，逻辑自洽但缺来源支持
